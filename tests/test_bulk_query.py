import pandas as pd
import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page, bulk_query
from flask_records import RecordsDao


@app.route('/bulk/users/c')
def bulk_create_user():
    users = [
        {'name': 'xc', 'age':1},
        {'name': 'yy', 'age':1}
    ]
    @bulk_query('INSERT INTO user(name, age) values (:name, :age)')
    def _bulk_create_user(users): 
        pass
    
    _bulk_create_user(users)

    return 'ok'


@app.route('/bulk/users/r')
def bulk_read_user():

    @query("SELECT * FROM user", True)
    def read_as_df():
        pass
    
    _type = isinstance(read_as_df().as_df(), pd.DataFrame)
    assert _type == True

    return 'ok'


class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()


class BulkTestCase(BasicTestCase):

    def test_1_create_bulk_users(self):
        self.app.get('/bulk/users/c')
        response = self.app.get('/bulk/users/r')
        assert response.data == b'ok'

if __name__ == '__main__':
    unittest.main()
