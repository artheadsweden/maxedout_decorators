from PreFunc import pre_func


def validate(in_str: str):
    if in_str.count(';') != 3:
        raise ValueError("Not 3 ; in string")
    return in_str


@pre_func(validate)
def parse(csv_str):
    values = csv_str.split(";")
    for item in values:
        print(item)

def reverse(*args):
    return tuple(a[::-1] for a in args)

@pre_func(reverse)
def add_strs(*args):
    return "-".join(*args)

def main():
    test_str = "Hi;there;all;folks"
    parse(test_str)

    print(add_strs("Apple", "Banana", "Citrus"))

if __name__ == '__main__':
    main()
