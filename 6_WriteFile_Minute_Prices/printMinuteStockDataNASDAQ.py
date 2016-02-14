import urllib2
import json
import urllib
import re
import os

#Daily Stock Price of Apple, NASDAQ Price Pull
#http://www.bloomberg.com/quote/AAPL:US
#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY


def main():

    # Chage working directory
    direct = "C:/Users/Julian/Documents/Python Scripts/PythonWebScraping/6_WriteFile_Minute_Prices/"
    os.chdir(direct)

    # Stringify words
    symbolslist = open("NASDAQ_Top100.txt").read()  
    symbolslist = symbolslist.split("\n")
        
    # For each of the Stock Symbols cycle through and print the list of prices
    for symbol in symbolslist:
        webURL = urllib2.urlopen('http://www.bloomberg.com/markets/api/bulk-time-series/price/'+symbol+':US?timeFrame=1_DAY').read()
        theJSON = json.loads(webURL)
   
        priceTimes = theJSON[0]["price"]
        timeNo = 0;
        
        for priceTime in priceTimes:
            print "symbol", symbol, "price", theJSON[0]["price"][timeNo]["value"], "time", theJSON[0]["price"][timeNo]["dateTime"]
            timeNo +=1
            

##      Tidy Directory                  ##
def filePathAndFiles():
    # Change the directory
    print   os.getcwd()
    print  os.listdir(os.curdir) #List files in current directory
    
    


##      Print Prices Only               ##
def printJSON(theJSON):
    stockprice = 0
    for values in theJSON[0]["price"]:
        print theJSON[0]["price"][stockprice]["value"]
        stockprice+=1
        
    #print "The number of prices is ", len(theJSON[0]["price"])


##      Print JSON of Prices and Times  ##
def printPriceTimes(theJSON):
    for values in theJSON[0]["price"]:
        print theJSON[0]["price"][priceTime]
        
        
    #print "The number of prices is ", len(theJSON[0]["price"])


if __name__ == "__main__":
    main()

##      Print first priceTime    ##
#   print theJSON[0]["price"][0]

##      Print the first price           ##
#   print theJSON[0]["price"][0]["value"]





