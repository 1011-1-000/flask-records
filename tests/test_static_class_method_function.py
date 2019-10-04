import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page
from flask_records import RecordsDao


@app.route('/dao/pagination/static/user/r/<int:page>')
def static_query_user(page):
    pagination = UserDao.query_user_by_page_with_static_method(page)
    return pagination.data[0].name


@app.route('/dao/pagination/cls/user/r/<int:page>')
def cls_query_user(page):
    pagination = UserDao().query_user_by_page_with_cls_method(page)
    return pagination.data[0].name


@app.route('/dao/pagination/func/user/r/<int:page>')
def function_query_user(page):
    pagination = query_user_by_page_with_function(page)
    return pagination.data[0].name


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()

    @staticmethod
    @query_by_page('SELECT * FROM user', True, page_size=2)
    def query_user_by_page_with_static_method(page):
        pass

    @query_by_page('SELECT * FROM user', True, page_size=2)
    def query_user_by_page_with_cls_method(self, page):
        pass


@query_by_page('SELECT * FROM user', True, page_size=2)
def query_user_by_page_with_function(page):
    pass


class PaginationTestCase(BasicTestCase):

    def test_1_query_by_page_with_static_method(self):
        self.app.get('/dao/user/c/xc/1')
        self.app.get('/dao/user/c/my/1')
        self.app.get('/dao/user/c/leo/18')

        response = self.app.get('/dao/pagination/static/user/r/1')
        assert b'xc' == response.data

        response = self.app.get('/dao/pagination/static/user/r/2')
        assert b'leo' == response.data

    def test_2_query_by_page_with_cls_method(self):

        response = self.app.get('/dao/pagination/cls/user/r/1')
        assert b'xc' == response.data

        response = self.app.get('/dao/pagination/cls/user/r/2')
        assert b'leo' == response.data

    def test_3_query_by_page_with_function(self):
        response = self.app.get('/dao/pagination/func/user/r/1')
        assert b'xc' == response.data

        response = self.app.get('/dao/pagination/func/user/r/2')
        assert b'leo' == response.data


if __name__ == '__main__':
    unittest.main()
