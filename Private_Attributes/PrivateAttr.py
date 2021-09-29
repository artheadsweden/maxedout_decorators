import inspect


def enforce_private(cls):

    def set_attr(self, key, value):

        if not key.startswith("_"):
            object.__setattr__(self, key, value)
        else:
            caller = inspect.stack()[1].function
            if caller not in dir(self):
                raise Exception(f"{key} is private")
            else:
                object.__setattr__(self, key, value)

    def get_attribute(self, item):
        caller = inspect.stack()[1].function
        if not item.startswith("_") or caller == 'get_attribute' or caller == 'set_attr':
            return object.__getattribute__(self, item)
        else:
            if caller not in dir(self):
                raise Exception(f"{item} is private")
            else:
                return object.__getattribute__(self, item)

    cls.__setattr__ = set_attr
    cls.__getattribute__ = get_attribute
    return cls


@enforce_private
class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


def main():
    person = Person('Jane', 43)
    person.age = 11
    print(person.age)
    # Accessing person._name will raise an exception
    # We will need to use access methods
    person.set_name('Anne')
    print(person.get_name())


if __name__ == '__main__':
    main()
