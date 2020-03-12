import functools
from tests.conftest import *


def log(original_function):
    @functools.wraps(original_function)
    def wrapper(*args, **kwargs):
        print("\n==>Test '%s' STARTED with positional arguments %s and keyword arguments %s.\n" % (
            original_function.__name__, args, kwargs))
        original_function(*args, **kwargs)
        print("\n==>Test '%s' COMPLETED.\n" % (original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper


# def is_active(token):
#     def decorator_is_active(original_function):
#         @functools.wraps(original_function)
#         def wrapper(*args, **kwargs):
#             if token != '':
#                 print('\neco_admin_access_token: ' + token)
#                 return original_function(*args, **kwargs)
#             return original_function(*args, **kwargs)
#         return wrapper
#     return decorator_is_active
