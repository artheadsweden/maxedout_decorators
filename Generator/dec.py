
def outer(f):
    def inner():
        return "<<<" + f() + ">>>"
    return inner

@outer
def hi():
    return "hi"


#hi = outer(hi)

s = hi()

print(s)