from Print import print


def main():
    x = 10
    print("x is", x)
    print("x", end="")
    print(x, start=" =")
    print(f"x is {x}", start="<", end=">\n", sep="")


if __name__ == '__main__':
    main()
