## Flask Records

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-records.svg)
[![Build Status](https://travis-ci.org/1011-1-000/flask-records.svg?branch=master)](https://travis-ci.org/1011-1-000/flask-records)

Flask-Records is an extension that manuiplate the DB with the raw sql for the flask application using records.

### Installation

> pip install flask-records

### Usage

#### Setup

Add the flask-records to your flask application.
```python
from flask import Flask
from flask_records import FlaskRecords

raw_db = FlaskRecords(app)
```
or initialize the app in the way below:
```python
from flask import Flask
from flask_records import FlaskRecords

raw_db = FlaskRecords()
raw_db.init_app(app)
```
#### Access DB With Flask Records

We have provided two decorators for easy using in the development:

##### query

The basic query decorator you can use in the flask records.

```python
from flask_records.decorators import query

@query("INSERT INTO users VALUES(:id, :name, :age)")
def hello_flask_records(id, name, age):
    pass

# call the function: hello_flask_records(1, 'Leo', 27)
```

also, you can wrap all the parameters in a dictionary and pass it to the function.
```python
from flask_records.decorators import query

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
```

##### query_by_page

This is the decorator which for the pagination.

```python
from flask_records.decorators import query_by_page

@query_by_page("SELECT * FROM users", 2)
def hello_flask_records(page):
    pass
```

### Extra Features

Flask-Records also provide the basic crud function, all you need to do is inherit the RecordsDao when you write the DAO layer classes.

```python
from flask_records import RecordsDao

class UserDao(RecordsDao):

    def __init__(self):
        super(UserDao, self).__init__()
```

For detailed instructions on the features, please refer to the flask records documentation.

- [Documentation](https://flask-records.readthedocs.io/en/latest/)

### ChangeLog

#### Release 0.0.15
- add a param converters in as_dict function, which means u can do the convertion according to your requirements. the format for this param is {'key': func}
- add bulk_query decorator, so you can insert multiple rows to the db
- add as_df function to the RecordCollection

#### Release 0.0.14
- Fix the initialize issue in the way like FlaskRecords()
- Modified the error in the Doc

#### Release 0.0.9
- Support the default params in the function when do the query
- Compatible with the Python2.7+ and 3.5+

#### Release 0.0.8
- Support the decorators on the function or method in the class
- Simplify the usage of the decorators
- Provide the base crud operations
- Add unit tests for the decorators, basic dao etc
