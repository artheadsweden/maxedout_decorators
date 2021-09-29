from to_dict import to_dict


@to_dict(['x', 'y', 'z'])
class A:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = [B(1), B(2)]

@to_dict(['value'])
class B:
    def __init__(self, value):
        self.value = value

def main():
    a = A()
    print(a.to_dict())


if __name__ == '__main__':
    main()
