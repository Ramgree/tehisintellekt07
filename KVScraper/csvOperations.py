import csv
import os
import fileinput
import copy

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
    for line in fileinput.input(FILENAME, inplace=1):
        print(line.upper(), end='')

if __name__ == '__main__':
    toUpperCase()
