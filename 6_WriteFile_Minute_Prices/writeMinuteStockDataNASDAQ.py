import urllib2
import json
import urllib
import re
import os

#Scrape NASDAQ top 100 minute prices and write to file
#http://www.bloomberg.com/quote/AAPL:US
#http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY


def main():

    # Chage working directory
    direct = "C:/Users/Julian/Documents/Python Scripts/PythonWebScraping/6_WriteFile_Minute_Prices/"
    os.chdir(direct)

    # Stringify words
    symbolslist = open("NASDAQ_Top100.txt").read()  
    symbolslist = symbolslist.split("\n")
        
    # For each of the Stock Symbols cycle through and write the minute updates to file 
    for symbol in symbolslist:

        # Dynamically name the file 
        myfile = open(direct + "daily_price/" + symbol + ".txt", "w+")
        myfile.close()
        
        webURL = urllib2.urlopen('http://www.bloomberg.com/markets/api/bulk-time-series/price/'+symbol+':US?timeFrame=1_DAY').read()
        theJSON = json.loads(webURL)

        myfile = open(direct + "daily_price/" + symbol + ".txt", "a")
        priceTimes = theJSON[0]["price"]
        timeNo = 0;
        for priceTime in priceTimes:
            myfile.write( str(symbol +","+ str(theJSON[0]["price"][timeNo]["value"]) +","+ str(theJSON[0]["price"][timeNo]["dateTime"]) +"\n" ))
            timeNo +=1
        myfile.close()
        print symbol + " written to file"



##      Tidy Directory                  ##
def filePathAndFiles():
    # Change the directory
    print   os.getcwd()
    print  os.listdir(os.curdir) #List files in current directory
    


if __name__ == "__main__":
    main()

##      Print first priceTime    ##
#   print theJSON[0]["price"][0]

##      Print the first price           ##
#   print theJSON[0]["price"][0]["value"]





