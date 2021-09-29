from PrivateAttr import enforce_private


@enforce_private
class A:
    def __init__(self):
        self._variable = 99
        self.x = 3

    def get_variable(self):
        return self._variable

    def method(self):
        print(self._variable)




def main():
    a = A()
    a._variable = 10
   # a.x = 10
    print(a.get_variable())
    a.method()
    print(a._variable)



if __name__ == '__main__':
    main()
