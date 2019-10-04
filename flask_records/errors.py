class Error(Exception):
    pass


class ParameterNotDefinedError(Error):

    def __init__(self, parameters):
        self.message = f'{parameters} is required'


class NotFoundFieldError(Error):

    def __init__(self, parameters, table):
        self.message = f'{parameters} is not in the {table} table'
