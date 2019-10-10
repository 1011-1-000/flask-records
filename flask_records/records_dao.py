import re
from sqlalchemy import inspect
from flask import current_app

from functools import wraps
from .decorators import query
from .errors import NotFoundFieldError


class RecordsDao(object):
    """
    The Basic Dao which provide the simple crud operations as default.
    """

    CREATE_SQL = 'INSERT INTO {}({}) VALUES({})'
    DELETE_SQL = 'DELETE FROM {} WHERE id = :id'
    UPDATE_SQL = 'UPDATE {} SET {} WHERE id = :id'
    SELECT_SQL = 'SELECT * FROM {} WHERE id = :id'

    def __init__(self):
        self.table_name = self._get_table_name()

    def create(self, attributes):
        """
        Create a new table record 
        """
        columns = list(attributes.keys())

        # will prevent the malicious code through this function
        self._check_dynamic_columns_in_raw_sql(columns)

        values = []
        for column in columns:
            values.append(':{column}'.format(column=column))

        @query(RecordsDao.CREATE_SQL.format(self.table_name, ','.join(columns), ','.join(values)))
        def _create(attributes):
            pass

        return _create(attributes)

    def delete(self, id):
        """
        Delete the record according to the id
        """
        @query(RecordsDao.DELETE_SQL.format(self.table_name))
        def _delete(id):
            pass

        return _delete(id)

    def update(self, attributes):
        """
        Update the record according to the id, the id need be contained in the attributes
        """
        columns = list(attributes.keys())
        columns.remove('id')
        # will prevent the malicious code through this function
        self._check_dynamic_columns_in_raw_sql(columns)

        column_assembly = []
        for column in columns:
            column_assembly.append(
                '{column} = :{column}'.format(column=column))

        @query(RecordsDao.UPDATE_SQL.format(self.table_name, ','.join(column_assembly)))
        def _update(attributes):
            pass

        return _update(attributes)

    def get(self, id):
        """
        Get the record according to the id
        """
        @query(RecordsDao.SELECT_SQL.format(self.table_name), True)
        def _get(id):
            pass

        return _get(id)

    def _check_dynamic_columns_in_raw_sql(self, column_parameters):
        """
        Check the columns is in db table or not.

        if there is the column which pass from client side is not in the table,
        raise the Exception to prevent in case the malicious code is executed.
        """
        db_table_columns = self._get_table_columns()
        difference = [
            column for column in column_parameters if column not in db_table_columns]
        if len(difference) > 0:
            raise NotFoundFieldError(','.join(difference), self.table_name)

    def _get_table_columns(self):
        """
        Refect the DB engine to get the metadata of the table
        """
        inspector = inspect(current_app.raw_db._engine)

        # solve the conflict on the user table
        _table_name = self._class_name_to_table_name_transformation()
        if _table_name == 'user':
            columns = inspector.get_columns(_table_name)
        else:
            columns = inspector.get_columns(self.table_name)

        columns = [column['name'] for column in columns]

        return columns

    def _get_table_name(self):
        """
        Get the table name according to the class name which should be written with CamelCase style.

        if the __tablename__ is specified, will use it as the table name else translate class name
        to table_name
        """
        try:
            table_name = self.__tablename__
        except AttributeError:
            table_name = self._class_name_to_table_name_transformation()
        except Exception:
            raise Exception('Failed to get the table_name')
        return table_name

    def _class_name_to_table_name_transformation(self):
        """
        tanslate the class name to the table name according to the named conventions

        1. split the class name with the capital letter

        2. if 'Dao' is included in the splitted array, will remove it, then join the elements
        in the array with '_' sign, and lower the string you get

        For example:
            CamelCase => camel_case
            CamelCaseDao => camel_case
            Camel => camel
        """
        name_array = re.split('([A-Z][a-z0-9]*)', self.__class__.__name__)
        exclude_key_words = ('', 'Dao')
        table_name_array = [
            name for name in name_array if name not in exclude_key_words]
        table_name = '_'.join(table_name_array).lower()
        return table_name
