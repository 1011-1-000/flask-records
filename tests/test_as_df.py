import pandas as pd
import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page
from flask_records import RecordsDao


@app.route('/as_df/user/c/<name>/<age>')
def as_df_create_user(name, age):
    UserDao().create({'name': name, 'age': 1})
    return 'OK'


@app.route('/as_df/users/r')
def as_df_read_user():

    @query("SELECT * FROM user", True)
    def read_as_df():
        pass
    
    _type = isinstance(read_as_df().as_df(), pd.DataFrame)
    assert _type == True

    return 'ok'


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()


class AsDfTestCase(BasicTestCase):

    def test_1_create_df(self):
        self.app.get('/as_df/user/c/yy/1')
        self.app.get('/as_df/user/c/xc/1')
        response = self.app.get('/as_df/users/r')
        assert response.data == b'ok'

if __name__ == '__main__':
    unittest.main()
