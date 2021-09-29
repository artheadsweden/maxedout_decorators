from Generic import generic

@generic
def first(x):
    print("first", x)


@first.register(list)
@first.register(dict)
def second(x):
    print("second", x)


@first.register(int)
def third(x):
    print("third", x)


@generic
def foo(a, b):
    print(f"foo({a}, {b})")


@foo.register(str)
def bar(a, b):
    print(f"bar({a}, {b})")



def main():
    first(1.2)
    first([1, 2])
    first({"key": "value"})
    first(1)

    #foo(1, 2)
    #foo("hi", "there")
    # We are only dispatching on the type of the first argument
    # so this call will execute bar()
    #foo("Hi", 3)


if __name__ == '__main__':
    main()
