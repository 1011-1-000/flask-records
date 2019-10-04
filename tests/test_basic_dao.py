import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page
from flask_records import RecordsDao


@app.route('/dao/user/c/<name>/<age>')
def dao_create_user(name, age):
    UserDao().create({'name': name, 'age': 1})
    return 'OK'


@app.route('/dao/user/r/<int:id>')
def dao_read_user(id):
    user = UserDao().get(id).first()
    if not user:
        return 'The user does not exist!'
    else:
        return user.name


@app.route('/dao/user/u/<id>/<name>')
def dao_update_user(id, name):
    UserDao().update({'id': id, 'name': 'my'})
    return 'OK'


@app.route('/dao/user/d/<id>')
def dao_delete_user(id):
    UserDao().delete(id)
    return 'OK'


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()


class DaoTestCase(BasicTestCase):

    def test_1_create_dao(self):
        response = self.app.get('/dao/user/c/xc/1')
        assert b'OK' == response.data

    def test_2_read_dao(self):
        response = self.app.get('/dao/user/r/1')
        assert b'xc' == response.data

    def test_3_update_dao(self):
        self.app.get('/dao/user/u/1/my')
        response = self.app.get('/dao/user/r/1')
        assert b'my' == response.data

    def test_4_delete_dao(self):
        self.app.get('/dao/user/d/1')
        response = self.app.get('/dao/user/r/1')

        self.assertEqual(b'The user does not exist!', response.data)


if __name__ == '__main__':
    unittest.main()
