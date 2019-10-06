import inspect
from types import MethodType


def is_func_or_static_method_in_decorator(func, *args):
    """
    determine if the func is the real func, static method or class method of the class

    If no args, it should be function or static method of the class

    if there are arguments, get the first argument and 
    try to validate if it contains the func.__name__ or not,
    if yes,  determine it with isinstance(attr, MethodType)
    else it should be a function or static method
    """
    is_function_or_static_method = True
    if len(args) > 0 and hasattr(args[0], func.__name__):
        attr = getattr(args[0], func.__name__)
        if isinstance(attr, MethodType):
            is_function_or_static_method = False

    return is_function_or_static_method


def _parse_signature(func, *args, **kwargs):
    """
    retrieve the parameters of the func, and organize as a dict to pass to the db engine
    """
    is_function_or_static_method = is_func_or_static_method_in_decorator(
        func, *args)

    parameters = list(inspect.signature(func).parameters.keys())

    def _parse_default(func):
        parameters = inspect.signature(func).parameters.values()
        for parameter in parameters:
            if parameter.default is not parameter.empty:
                kwargs[parameter.name] = parameter.default

        return kwargs

    if not is_function_or_static_method:
        parameters.pop(0)
        _, *args = args

    kwargs = _parse_default(func)

    for parameter, value in zip(parameters, args):
        if isinstance(value, dict):
            kwargs.update(value)
        else:
            kwargs.update({parameter: value})

    return kwargs
