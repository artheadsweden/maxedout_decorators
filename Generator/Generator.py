def generator(cond):
    def decorator(f):
        def wrapper(n):
            while n < cond:
                yield f(n)
                n += 1
        return wrapper
    return decorator
