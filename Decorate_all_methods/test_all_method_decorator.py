from Time_it import time_it
from time import sleep


class A:
    @time_it
    def a(self): sleep(0.5)

    @time_it
    def b(self): sleep(0.5)

    @time_it
    def c(self): sleep(0.5)

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(time_it)
class B:
    def a(self): sleep(0.5)
    def b(self): sleep(0.5)
    def c(self): sleep(0.5)

def main():
    a = A()
    a.a()
    a.b()
    a.c()

    b = B()
    b.a()
    b.b()
    b.c()


if __name__ == '__main__':
    main()
