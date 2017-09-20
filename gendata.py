import csv
import datetime
#import histdata
import news
import sentiment
import sys

#csv.field_size_limit(sys.maxint)

def fetchData():
    #print 'Updating historical stock data'
    #histdata.getHistData()

    print ('Updating news data')
    #news.init()

def getStockData(symbol, date):
    file = open('data/hsd/' + symbol + '.csv')
    csv_file = csv.reader(file)

    # Get stock data for the next day
    date += datetime.timedelta(days=1)

    data = []

    #print 'Getting stock data for %s for date %s' % (symbol, date.strftime('%Y-%m-%d'))

    for row in csv_file:
        if(row[0] == date.strftime('%Y-%m-%d')):
            data.append(float(row[1]))
            data.append(float(row[4]))
            return data

    # No data found for symbol for given date
    return -1

def genData():
    #dataHistFile = open('dat.pkl', 'r+b')
    #dataHist = pickle.load(dataHistFile)
    #dataFileNumber = dataHist['data_file_number'] + 1

    #dataFile = open('data/dat_' + dataFileNumber + '.csv', 'a')
    dataFile = open('data/dat_9.csv', 'a')
    csvWriter = csv.writer(dataFile)
    #date = dateHist['last_updated']
    #endDate = datetime.date.today()
    date = datetime.datetime.strptime('27012014', "%d%m%Y").date()
    endDate = datetime.datetime.strptime('01012017', "%d%m%Y").date()

    c = csv.reader(open('dict.csv','r'))
    dic = {}
    for rw in c:
        dic[rw[1]] = rw[0]

    while(date < endDate):
        #print 'Checking data for ' + date.strftime('%Y-%m-%d')

        day = date.weekday()
        if(day == 4 or day == 5):
            date += datetime.timedelta(days=1)
            continue

        fname = date.strftime('%Y-%m-%d')
        file = open('data/news1/' + fname + '.csv')
        csv_file = csv.reader(file)

        for row in csv_file:
            stockdata = getStockData(dic[row[0]], date)
            if(stockdata == -1):
                continue
            t = ''
            news = t.join(row[1:])
            #print (news)
            pos, neg = sentiment.analyzeText(news)

            data = []
            data.extend((row[0], date.timetuple().tm_yday))
            data.append(pos)
            data.append(neg)
            data.extend(stockdata)
            csvWriter.writerow(data)

        date += datetime.timedelta(days=1)

    #dataHist['data_file_number'] = dataFileNumber
    #dataHist['last_updated'] = endDate
    #dataHistFile.seek(0)
    #pickle.dump(dataHist, dataHistFile, protocol = pickle.HIGHEST_PROTOCOL)
    #dataHistFile.close()

def init():
    #fetchData()
    genData()

init()
