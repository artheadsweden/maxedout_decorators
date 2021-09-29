from Func_attr import func_attr


@func_attr(author="Anna", date="2019-02-23")
def a():
    pass


@func_attr(author="Bob", date="2019-01-23")
def b(): pass


def main():
    print(a.author)
    print(a.date)

    print(b.author)
    print(b.date)


if __name__ == '__main__':
    main()
