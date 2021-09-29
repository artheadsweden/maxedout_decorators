from Generator import generator

@generator(8)
def abc(x):
    return x + 1

def main():
    for i in abc(1):
        print(i)


if __name__ == '__main__':
    main()
