class Error(Exception):
    pass


class ParameterNotDefinedError(Error):

    def __init__(self, parameters):
        self.message = '{} is required'.format(parameters)


class NotFoundFieldError(Error):

    def __init__(self, parameters, table):
        self.message = '{} is not in the {} table'.format(parameters, table)
