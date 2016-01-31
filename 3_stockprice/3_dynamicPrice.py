#Web Scraper to Get the prices of a list of ASX200 Stocks
#Symbols obtained fron a file input
#Python 2.7.2
#JWise

import urllib   #interface with urls
import re       #regex library

symbolfile = open("symbols.txt")
symbolslist = symbolfile.read()

stockSymbolList = symbolslist.split("\n")



i = 0
while i < len(stockSymbolList):
    url = "https://au.finance.yahoo.com/q?p=finance.yahoo.com&d=t&s=" + stockSymbolList[i] + ".AX"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*.ax">(.+?)</span>' #regex in brackets [^.]3 = new string any chars, any number of times
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print"The price of ", stockSymbolList[i], " is $", price
    i+=1
