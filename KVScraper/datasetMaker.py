import urlBuilder as ub
import pageParser as pp
import csvOperations as co

FIELDNAMES = ['area', 'price', 'state', 'city', 'district', 'link']


def makeDataSet():
    co.makeCSVfile()
    url = ub.make_url()
    pages = ub.count_pages(url)
    for i in range(1, pages+1):
        url = ub.make_url(i)
        pp.page_parser(url)


if __name__ == '__main__':
    makeDataSet()
