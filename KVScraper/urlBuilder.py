# hello world mem
from urllib import request
from bs4 import BeautifulSoup as bf


BASE_URL = "https://www.kv.ee/?act=search.simple"
PAGE_SIZE = 100
DEAL_TYPE = 6  # üür


def make_url(page_number: int = 1):
    return BASE_URL + "&page=%d&page_size=%d&deal_type=%d" % (page_number, PAGE_SIZE, DEAL_TYPE)


def count_pages(url):
    content = request.urlopen(url)
    raw_html = content.read()
    soup = bf(raw_html, 'html.parser')
    tag = soup.select('.jump-pagination-list > li:nth-of-type(3)')[0]
    return int(tag.text)
