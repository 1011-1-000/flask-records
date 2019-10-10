import os
import unittest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_records import FlaskRecords
from flask_records.decorators import query, query_by_page
from flask_records.records_dao import RecordsDao

basedir = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/app.db'.format(basedir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
raw_db = FlaskRecords(app)
# raw_db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)


class BasicTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # pass
        db.session.remove()
        db.drop_all()
