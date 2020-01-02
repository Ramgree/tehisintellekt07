import csv

FIELDNAMES = ['area', 'price', 'state', 'city', 'district','year','condition','energyscore', 'link']

def makeCSVfile():
    csvfile = open('kvObjects.csv', 'w')
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writeheader()

def writeRow(information):
    csvfile = open('kvObjects.csv', 'a')
    writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
    writer.writerow(
        {'area': information['area'], 'price': information['month_price'],
         'state': information['state'], 'city': information['city'], 'district': information['district'],
         'year' : information['year'], 'condition' : information['condition'], 'energyscore' : information['energyscore'],
          'link': information['link']})
