import inspect


class A:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, item):
        caller = inspect.stack()[1].function
        if caller == '__getattribute__':
            return object.__getattribute__(self, item)
        x = inspect.stack()
        if caller in dir(self):
            print(f"From self {caller} and {item}")
            return object.__getattribute__(self, item)
        print(f"Not from self {caller} and {item}")
        return object.__getattribute__(self, item)

    def test(self):
        a = self.x

a = A()
f = a.x
a.test()


