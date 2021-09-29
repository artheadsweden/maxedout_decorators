import inspect
import sys
from functools import wraps

def sync(lock):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            with lock:
                return f(*args, **kwargs)
        return wrapper
    return decorator


def private_old(method):
    class_name = inspect.stack()[1][3]

    @wraps(method)
    def privatized_method(*args, **kwargs):
        call_frame = inspect.stack()[1][0]

        # Only methods of same class should be able to call
        # private methods of the class, and no one else.
        if 'self' in call_frame.f_locals:
            caller_class_name = call_frame.f_locals['self'].__class__.__name__
            if caller_class_name == class_name:
                return method(*args, **kwargs)
        raise TypeError("can't call private method")

    return privatized_method


def private(member):
    @wraps(member)
    def wrapper(*args, **kwargs):
        myself = member.__name__
        caller = inspect.stack()[1][0].f_code.co_name
        if not caller in dir(args[0]) and not caller is myself:
            raise Exception(f"{myself} called by {caller} is private")
        return member(*args, **kwargs)

    return wrapper