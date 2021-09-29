
dec = lambda f: lambda *ar, **kw: "*** " + f(*ar, **kw) + " ***"


@dec
def greeting(greet, name):
    return f"{greet} {name}!"


def main():
    print(greeting("Yo", "Anna"))
    print(greeting.__name__)

if __name__ == '__main__':
    main()
