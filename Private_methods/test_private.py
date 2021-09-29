from Private import private


class A:
    def __init__(self):
        self.variable = 0

    @private
    def priv_method(self):
        print("a")

    def pub_method(self):
        self.priv_method()

class B(A):
    def b_pub(self):
        self.priv_method()



def main():
    a = B()
    a.priv_method()
    a.b_pub()



if __name__ == '__main__':
    main()
