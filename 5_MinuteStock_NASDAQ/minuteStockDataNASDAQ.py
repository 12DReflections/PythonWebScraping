import urllib2
import json

#Daily Stock Price of Apple, NASDAQ Price Pull
#http://www.bloomberg.com/quote/AAPL:US
#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY


def main():
    webURL = urllib2.urlopen("http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY").read()
    theJSON = json.loads(webURL)
    printJSON(theJSON)
    #printPriceTimes(theJSON)


##      Print Prices Only               ##
def printJSON(theJSON):
    stockprice = 0
    for values in theJSON[0]["price"]:
        print theJSON[0]["price"][stockprice]["value"]
        stockprice+=1
        
    #print "The number of prices is ", len(theJSON[0]["price"])


##      Print JSON of Prices and Times  ##
def printPriceTimes(theJSON):
    priceTime = 0
    for values in theJSON[0]["price"]:
        print theJSON[0]["price"][priceTime]
        priceTime+=1
        
    #print "The number of prices is ", len(theJSON[0]["price"])


if __name__ == "__main__":
    main()

##      Print first priceTime    ##
#   print theJSON[0]["price"][0]

##      Print the first price           ##
#   print theJSON[0]["price"][0]["value"]





