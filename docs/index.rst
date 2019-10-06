.. Flask-Records documentation master file, created by
   sphinx-quickstart on Sat Oct  5 20:25:42 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-Records
=============
Flask-Records is an extension that manuiplate the DB with the raw sql for the flask application using records.

Installation
------------
Install flask-records with command `pip`::

    pip install flask-records

Setup
-----
Add the flask-records to your flask application::

    from flask import Flask
    from flask_records import FlaskRecords
    raw_db = FlaskRecords(app)

or initialize the app in the way below::

    from flask import Flask
    from flask_records import FlaskRecords

    raw_db = FlaskRecords()
    raw_db.init_app(app)

Decorators
----------
We have provided two decorators for easy using in the development.

- **@query**, the basic query decorator you can use in the flask records, there are two parameters for this decorator.
    - **sql**: the raw sql that you want to execute.
    - **fetchall**: the parameters that control lazy fetching data from the database or not, the default value is false.

    Here is an example::

        from flask_records.decorator import query

        @query("INSERT INTO users VALUES(:id, :name, :age)")
        def hello_flask_records(id, name, age):
            pass

        # call the function: hello_flask_records(1, 'Leo', 27)

    Also, you can wrap all the parameters in a dictionary and pass it to the function.
    ::

        from flask_records.decorator import query

        @query( "INSERT INTO users VALUES(:id, :name, :age)")
        def hello_flask_records(parameters):
            pass

        # define a dict which contains the query parameters
        # parameters = {
        #     'id': 1,
        #     'name': 'Leo', 
        #     'age': 27
        # }
        # call the function: hello_flask_records(parameters)

- **@query_by_page**, easy to understand what's the decorator using forfrom it's name.

    - **sql**: the raw sql that you want to execute.
    - **fetchall**: the parameters that control lazy fetching data from the database or not, the default value is false.
    - **page_size**: the number of elements per page.

    for example::

        from flask_records.decorator import query_by_page

        @query_by_page("SELECT * FROM users", 2)
        def hello_flask_records(page):
            pass

    the return value is an pagination object, which has the attributes: total, data, page, page_size, last_page

**tips**: need to specify the **page** parameter in the function args or in the parameter dict when use this decorator.

Data Access Operations
----------------------

Flask-Records also provide the basic crud functions, all you need to do is inherit the RecordsDao when you write the DAO layer classes.
::

    from flask_records import RecordsDao

    class UserDao(RecordsDao):

        def __init__(self):
            super(UserDao, self).__init__()

RecordsDao will get the table name automatically according to the class name camel case convention. For example:

- CamelCase => camel_case
- CamelCaseDao => camel_case
- Camel => camel

also, you can specify the table name when you define the Dao class.::

    from flask_records import RecordsDao

    class UserDao(RecordsDao):
        __tablename__ = 'public.user'

        def __init__(self):
            super(UserDao, self).__init__()

RecordsDao will use the __tablename__ as the table name when submit the crud operations.


- ``create(self, attributes)``
    Create a new table record

- ``get(self, id)``
    Get the record according to the id

- ``update(self,attributes)``
    Update the record according to the id, the id need be contained in the attributes

- ``delete(self, id)``
    Delete the record according to the id

