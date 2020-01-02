from urllib import request  # u tebya tam reqrequst bql   m e h
from bs4 import BeautifulSoup as bf  # srsly?
import re
import string
import pageParser as pp


def getParameter(tag, type):
    try:
        text = tag.find("th", text=type).find_next_sibling("td").text
        stripped = format(text.strip())
        # print(text)
        return stripped
    except:
        return ""

def format(text):
    chars = re.escape(string.punctuation)
    return re.sub(r'['+chars+']', '',text).replace("Puudub","")

def getInfo(res):
    year = getParameter(res, "Ehitusaasta")
    condition = getParameter(res, "Seisukord")
    energyScore = getParameter(res, "Energiamärgis")
    return [year, condition, energyScore]


def advertismentParser(url):
    content = request.urlopen(url)
    raw_html = content.read()
    soup = bf(raw_html, 'html.parser')
    res = soup.find(class_="table-lined object-data-meta")
    return getInfo(res)
