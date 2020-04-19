import inspect
from functools import wraps
from collections import namedtuple
from flask import current_app
from ._internals import _parse_signature
from .errors import ParameterNotDefinedError


Pagination = namedtuple(
    'Pagination', ['data', 'total', 'is_last_page', 'page', 'page_size'])


def query(sql, fetchall=False):
    def db_query(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # print(_parse_signature(func, args, kwargs))
            parameters = _parse_signature(func, *args, **kwargs)
            results = current_app.raw_db.query(sql, fetchall, **parameters)
            return results
        return wrapper
    return db_query

def bulk_query(sql, fetchall=False):
    def db_query(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = current_app.raw_db.bulk_query(sql, *args)
            return results
        return wrapper
    return db_query

def query_by_page(sql, fetchall=False, page_size=10):
    def db_query(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parameters = _parse_signature(func, *args, **kwargs)
            page = parameters.get('page', None)
            if not page:
                raise ParameterNotDefinedError('page')

            data, total, is_last_page = current_app.raw_db.query_by_page(
                sql, int(page), int(page_size), fetchall, parameters)

            pagination = Pagination._make(
                [data, total, is_last_page, page, page_size])
            return pagination
        return wrapper
    return db_query
