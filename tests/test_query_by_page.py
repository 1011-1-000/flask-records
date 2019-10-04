import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page
from flask_records import RecordsDao


# @app.route('/dao/user/c/<name>/<age>')
# def dao_create_user(name, age):
#     UserDao().create({'name': name, 'age': age})
#     return 'OK'


@app.route('/dao/pagination/user/r/<int:page>')
def query_user(page):
    pagination = UserDao().query_user_by_page(page)
    return pagination.data[0].name


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()

    @query_by_page('SELECT * FROM user', True, page_size=2)
    def query_user_by_page(self, page):
        pass


class PaginationTestCase(BasicTestCase):

    def test_query_by_page(self):
        self.app.get('/dao/user/c/xc/1')
        self.app.get('/dao/user/c/my/1')
        self.app.get('/dao/user/c/leo/18')

        response = self.app.get('/dao/pagination/user/r/1')
        assert b'xc' == response.data

        response = self.app.get('/dao/pagination/user/r/2')
        assert b'leo' == response.data


if __name__ == '__main__':
    unittest.main()
