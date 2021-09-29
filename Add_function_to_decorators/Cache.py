from functools import wraps
from collections import Hashable

def cache(f):
    the_cache = {}

    @wraps(f)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in the_cache:
            result = f(*args, **kwargs)
            the_cache[key] = result
        return the_cache[key]

    def clear():
        nonlocal the_cache
        the_cache = {}

    wrapper.clear = clear
    return wrapper
