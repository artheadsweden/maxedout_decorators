import time
from threading import Thread
from functools import wraps


def timer(delay, repetitions=None):
    def decorator(f):
        def timer_thread(args, kwargs):
            if repetitions is not None:
                for _ in range(repetitions):
                    time.sleep(delay)
                    f(*args, **kwargs)
            else:
                while True:
                    time.sleep(delay)
                    f(*args, **kwargs)

        @wraps(f)
        def wrapper(*args, **kwargs):
            thread = Thread(target=timer_thread, args=(args, kwargs))
            thread.start()
        return wrapper

    return decorator
