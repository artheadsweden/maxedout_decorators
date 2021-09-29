def pre_func(pre):
    def decorator(f):
        def wrapper(*args, **kwargs):
            try:
                result = pre(*args, **kwargs)
            except Exception as e:
                print("Got an exception:", e)
                return None
            return f(result)
        return wrapper
    return decorator
