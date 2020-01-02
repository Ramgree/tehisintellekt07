from urllib import request  # u tebya tam reqrequst bql   m e h
from bs4 import BeautifulSoup as bf  # srsly?
import re


def page_parser(url):
    content = request.urlopen(url)
    raw_html = content.read()
    soup = bf(raw_html, 'html.parser')
    objects = soup.find_all("tr", class_='object-item')
    return parse_objects(objects)


def parse_objects(objects):
    information = []
    for object in objects:
        information.append(parse_single_object(object))
    return information


def parse_single_object(object):
    area = getInfo(object, "object-m2")
    month_price = getInfo(object, "object-price-value")
    location, link = getAddress(object)

    address = location.split(",")
    state = address[0]
    city = address[1]
    if len(address) < 4:
        return area, month_price, state, city, "", link
    distict = address[2]
    return area, month_price, state, city, distict, link


def getInfo(tag, type):
    res = tag.find(class_=type)
    return format(res.text)


def getAddress(tag):
    res = tag.find(class_="object-title-a")
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
