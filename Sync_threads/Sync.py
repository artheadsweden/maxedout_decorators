from functools import wraps

def sync(lock):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            with lock:
                return f(*args, **kwargs)
        return wrapper
    return decorator
