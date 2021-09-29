from time import time
from functools import wraps


def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        stop = time()
        print(f"Call to {f.__name__} took {stop-start} seconds")
        return result
    return wrapper