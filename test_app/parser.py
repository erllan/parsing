import requests
from bs4 import BeautifulSoup


def requests_parser(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(url.url, headers=header)
    r.encoding = 'utf-8'
    result = []
    b = BeautifulSoup(r.text, 'html.parser')
    h1 = b.find_all('h1')
    title = b.find_all('title')
    result.append(title)
    result.append(h1)
    url.resulturl_set.create(title=title, h1=h1)
    return result
