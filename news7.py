from bs4 import BeautifulSoup
import pickle
import datetime
import requests

FNAME = "snp500_formatted.txt"
stocks = []

def getNewsForDate(date):
    file = open('data/news1/' + date.strftime('%Y-%m-%d') + '.csv', 'wb')
    print('Getting news for ' + date.strftime('%Y-%m-%d'))
    for i in range(len(stocks)):
        query = 'http://www.reuters.com/finance/stocks/company-news/' + stocks[i] + '?date=' + format(date.month, '02d') + format(date.day, '02d') + str(date.year)
        print('Getting news for ' + query)

        response = requests.get(query)
        soup = BeautifulSoup(response.text, "html.parser")
        divs = soup.findAll('div', {'class': 'feature'})
        print('Found ' + str(len(divs)) + ' articles.')

        if(len(divs) == 0):
            continue

        data = []
        for div in divs:
            data += div.findAll(text=True)
            data += ["~"]
        t = u''
        data = t.join(data)
        file.write((stocks[i] + ',' + data.replace('\n', ' ') + '\n').encode('utf-8'))
    file.close()

def getNews():
    year = datetime.timedelta(days=365)
    day = datetime.timedelta(days=1)
    endDate = datetime.date.today()
    date = endDate - 2*year - 143*day
    endDate = endDate - 2*year - 141*day

    while(date <= endDate):
        getNewsForDate(date)
        date += datetime.timedelta(days=1)

def init():
    global stocks
    with open(FNAME) as f:
        stocks = f.readlines()
    for i in range(len(stocks)):
        stocks[i] = stocks[i].rstrip('\n')

    getNews()

