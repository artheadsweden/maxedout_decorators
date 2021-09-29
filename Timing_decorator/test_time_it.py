from Time_it import time_it
from time import sleep


@time_it
def time_me(s):
    sleep(s)


def main():
    time_me(3)


if __name__ == '__main__':
    main()
