from functools import wraps


def func_attr(**kwrd):
    def func_dec(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            return f(*args, **kwargs)

        if len(kwrd) == 0:
            raise TypeError(f"No new attributes provided for {f.__name__}")
        for k, v in kwrd.items():
            setattr(wrapper, k, v)

        return wrapper
    return func_dec
