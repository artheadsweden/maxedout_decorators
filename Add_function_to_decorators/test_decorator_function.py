from Time_it import time_it
from Cache import cache
import requests


@time_it
@cache
def get_page(url):
    return requests.get(url).text


def main():
    get_page('http://python.org')

    get_page('http://python.org')

    get_page.clear()

    get_page('http://python.org')


if __name__ == '__main__':
    main()
