import requests
from bs4 import BeautifulSoup


def requests_parser(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    return r


def parser_html(html, teg):
    b = BeautifulSoup(html, 'html.parser')
    items = b.find_all(teg)
    return items
