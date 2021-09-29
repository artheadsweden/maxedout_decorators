import inspect
from functools import wraps


def private(member):
    @wraps(member)
    def wrapper(*args, **kwargs):
        myself = member.__name__
        caller = inspect.stack()[1].function
        self = args[0]

        if caller not in dir(self):
            raise Exception(f"{myself} called by {caller} is private")
        return member(*args, **kwargs)

    return wrapper


class TestClass(object):
    @private
    def private_method(self):
        print("Inside the private method")

    def public_method(self):
        self.private_method()


def main():
    test_obj = TestClass()
    test_obj.public_method()


if __name__ == '__main__':
    main()
