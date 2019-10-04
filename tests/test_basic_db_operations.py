import unittest
from tests.app import app, db, BasicTestCase
from flask_records.decorators import query, query_by_page


@app.route('/basic/user/c/<name>/<age>')
def create_user(name, age):
    basic_create_user(name, age)
    return 'OK'


@app.route('/basic/user/r/<id>')
def read_user(id):
    user = get_user_by_id(id).first()
    if not user:
        return 'The user does not exist!'
    else:
        return user.name


@app.route('/basic/user/u/<id>/<name>')
def update_user(id, name='my'):
    update_user_by_id(id, name)
    return 'OK'


@app.route('/basic/user/d/<id>')
def delete_user(id):
    delete_user_by_id(id)
    return 'OK'


@query("INSERT INTO user(name, age) VALUES (:name, :age)")
def basic_create_user(name, age):
    pass


@query("SELECT * FROM user WHERE id = :id", True)
def get_user_by_id(id):
    pass


@query("UPDATE user SET name = :new_name WHERE id = :id")
def update_user_by_id(id, new_name):
    pass


@query("DELETE FROM user where id = :id")
def delete_user_by_id(id):
    pass


class TestCase(BasicTestCase):

    def test_1_create(self):
        # create user xc with 1 age
        response = self.app.get('/basic/user/c/xc/1')
        assert b'OK' == response.data

    def test_2_read(self):
        response = self.app.get('/basic/user/r/1')
        assert b'xc' == response.data

    def test_3_update(self):
        self.app.get('/basic/user/u/1/my')
        response = self.app.get('/basic/user/r/1')
        assert b'my' == response.data

    def test_4_delete(self):
        self.app.get('/basic/user/d/1')
        response = self.app.get('/basic/user/r/1')
        self.assertEqual(b'The user does not exist!', response.data)


if __name__ == '__main__':
    unittest.main()
