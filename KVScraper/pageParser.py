from urllib import request  # u tebya tam reqrequst bql   m e h
from bs4 import BeautifulSoup as bf  # srsly?
import re
import advertisementParser as ap
import csvOperations as co

def page_parser(url):
    content = request.urlopen(url)
    raw_html = content.read()
    soup = bf(raw_html, 'html.parser')
    objects = soup.find_all('tr', class_='object-item')
    parse_objects(objects)


def parse_objects(objects):
    information = []
    for object in objects:
        co.writeRow(parse_single_object(object))


def parse_single_object(object):
    all_info = {}

    all_info['area'] = getInfo(object, 'object-m2')
    all_info['month_price'] = getInfo(object, 'object-price-value')
    location, all_info['link'] = getAddress(object)

    address = location.split(',')
    all_info['state'] = address[0]
    all_info['city'] = address[1]

    all_info['year'], all_info['condition'], all_info['energyscore'] = ap.advertismentParser(all_info['link'])

    if len(address) < 4:
        all_info['district'] = ''
        return all_info
    all_info['district'] = address[2]
    return all_info


def getInfo(tag, type):
    res = tag.find(class_=type)
    return format(res.text)


def getAddress(tag):
    res = tag.find(class_='object-title-a')
    link = res.get('href')
    text = res.text
    location = text.strip().replace(u'\xa0', '')
    return location, link


def format(text):
    try:
        stripped = text.strip().replace(u'\xa0', '')
        formatted = re.findall(r'\d+', stripped)
        return formatted[0]
    except:
        return None

# PACK/\ADKY HE MEH9||-0
# спать не хочешь еще?
# HET  вот прям капсом?
# Я тебе в этом плане даже завидую немного
