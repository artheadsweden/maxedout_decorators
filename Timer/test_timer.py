from Timer import timer


@timer(3, 5)
def print_greeting(greeting, name):
    print(f"{greeting}, {name}!")


@timer(1)
def print_hi(name):
    print(f"Hi {name}!")


def main():
    print_greeting('Hello', 'Alice')
    print_hi('Bob')


if __name__ == '__main__':
    main()
