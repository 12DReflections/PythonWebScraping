#Web Scraper to Get the prices of a list of ASX Stocks
#Python 2.7.2
#Use easiest way to prevent needing to change the whole way on a site update
#JWise

symbolslist = ["cba", "anz", "wbc", "nab"] 

import urllib   #interface with urls
import re       #regex library

i = 0
while i < len(symbolslist):
    url = "https://au.finance.yahoo.com/q?p=finance.yahoo.com&d=t&s=" + symbolslist[i] + ".AX"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_'+symbolslist[i]+'.ax">(.+?)</span>' #regex in brackets
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print"The price of ", symbolslist[i], " is $", price[0]
    i+=1
