import csv
import urlBuilder as ub
import pageParser as pp


def makeDataSet():
    with open('kvObjects.csv', 'w') as csvfile:
        url = ub.make_url()
        pages = ub.count_pages(url)

        fieldnames = ['area', 'price', 'state', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, pages+1):
            url = ub.make_url(i)
            data = pp.page_parser(url)
            for j in range(len(data)):
                object = data[j]
                writer.writerow(
                    {'area': object[0], 'price': object[1], 'state': object[2], 'link': object[3]})


if __name__ == '__main__':
    makeDataSet()
