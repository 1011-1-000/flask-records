import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page
from flask_records import RecordsDao

def upper(s): 
    return s.upper()

@app.route('/converter/user/c/<name>/<age>')
def converter_create_user(name, age):
    UserDao().create({'name': name, 'age': 1})
    return 'OK'


@app.route('/converter/user/r/<int:id>')
def converter_read_user(id):
    user = UserDao().get(id).first().as_dict({'name': upper})
    if not user:
        return 'The user does not exist!'
    else:
        return user.get('name')


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()


class ConverterTestCase(BasicTestCase):

    def test_1_create_converter(self):
        response = self.app.get('/converter/user/c/xc/1')
        assert b'OK' == response.data

    def test_2_read_converter(self):
        response = self.app.get('/converter/user/r/1')
        assert b'XC' == response.data


if __name__ == '__main__':
    unittest.main()
