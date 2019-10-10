import os
from records import Database


class FlaskRecords(Database):

    def __init__(self, flask_app, **kwargs):
        self.db_url = flask_app.config['SQLALCHEMY_DATABASE_URI'] or os.environ.get(
            'DATABASE_URL')
        super(FlaskRecords, self).__init__(self.db_url, **kwargs)
        flask_app.raw_db = self

    def init_app(self, flask_app, **kwargs):
        self.db_url = flask_app.config['SQLALCHEMY_DATABASE_URI'] or os.environ.get(
            'DATABASE_URL')
        super(FlaskRecords, self).__init__(self.db_url, **kwargs)
        flask_app.raw_db = self

    def query_by_page(self, sql, page, page_size, fetchall, params):
        counts = "SELECT COUNT(*) FROM ({}) AS tmp".format(sql)
        current_page_sql = "{} LIMIT {} OFFSET {}".format(
            sql, page_size, (page - 1) * page_size)
        with self.get_connection() as conn:
            total = conn.query(counts, fetchall, **params).scalar()
            data = conn.query(current_page_sql, fetchall, **params)
            is_last_page = page * page_size >= total
        return data, total, is_last_page
