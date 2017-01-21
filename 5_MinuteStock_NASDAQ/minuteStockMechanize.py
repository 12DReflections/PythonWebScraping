import json
import urllib2
import mechanize
import logging
from mechanize import Browser

# Use mechanize to hide as a browser and view the stock updates
# Websites cannot see this as a bot


def main():
	ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
	mechBrowser = Browser()
	mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
	mechBrowser.set_debug_http(True)
	mechBrowser.set_debug_responses(True)
	logging.getLogger('mechanize').setLevel(logging.DEBUG)
	feed = mechBrowser.open('http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY').read()
	theJSON = json.loads(feed)
    	printJSON(theJSON)

#refine
##      Print Prices Only               ##
def printJSON(theJSON):
    stockprice = 0
    for values in theJSON[0]["price"]:
        print theJSON[0]["price"][stockprice]["value"]
        stockprice+=1
