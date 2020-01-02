import csv
import os
import pandas as pd
import numpy as np

FILENAME = 'kvObjects.csv'

FIELDNAMES = ['area', 'price', 'state', 'city',
              'district', 'year', 'condition', 'energyscore', 'link']


def makeCSVfile():
    csvfile = open(FILENAME, 'w')
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writeheader()


def writeRow(information):
    csvfile = open(FILENAME, 'a')
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writerow(
        {'area': information['area'], 'price': information['month_price'],
         'state': information['state'], 'city': information['city'], 'district': information['district'],
         'year': information['year'], 'condition': information['condition'], 'energyscore': information['energyscore'],
         'link': information['link']})


def toUpperCase():
    data = pd.read_csv(FILENAME)
    data.columns = map(str.upper, data.columns)
    data = data.applymap(lambda s: s.upper() if type(s) == str else s)
    data['LINK'] = data['LINK'].str.lower()
    data['AREA'] = data['AREA'].apply(lambda x: int(x) if x == x else "")
    data['YEAR'] = data['YEAR'].apply(lambda x: int(x) if x == x else "")
    data.to_csv(FILENAME, index=False)


if __name__ == '__main__':
    toUpperCase()
