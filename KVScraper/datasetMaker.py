import csv
import urlBuilder as ub
import pageParser as pp


def makeDataSet():
    with open('kvObjects.csv', 'w') as csvfile:
        url = ub.make_url()
        pages = ub.count_pages(url)

        fieldnames = ['area', 'price', 'state', 'city', 'district', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, pages+1):
            url = ub.make_url(i)
            data = pp.page_parser(url)
            for j in range(len(data)):
                object = data[j]
                area = object[0]
                price = object[1]
                state = object[2]
                city = object[3]
                district = object[4]
                link = object[5]
                writer.writerow(
                    {'area': area, 'price': price, 'state': state, 'city': city, 'district': district, 'link': link})


if __name__ == '__main__':
    makeDataSet()
