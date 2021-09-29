def c():
    r = 10/0


def b():
    c()


def a():
    b()


def main():
    a()


main()

