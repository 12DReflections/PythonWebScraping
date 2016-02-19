import json
import urllib2
import mechanize
import logging
from mechanize import Browser
import re

# Pull flight data from web
# Source:		https://www.flightradar24.com/60.8,84.57/2
# Direct Link:	https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&

# trial 'http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY'

def main():
	# Set up Mechanize Browser 
	ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
	mechBrowser = Browser()
	mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
	#debug(mechBrowser) 

	feed = mechBrowser.open('https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&').read()
	theJSON = json.loads(feed)
    	
    	printJSON(theJSON) # Bug in JSON library causing indentation error

def printJSON(theJSON):
    planeTotal = theJSON["full_count"]
    '''
    strJSON = json.dumps(theJSON)   # A string version of the JSON to test the regular expression
    regex = ', "(8d.+7)": \["'         #Regex pattern
    pattern = re.compile(regex)
    planeList = re.findall(pattern, strJSON)
    '''    
# plane id:  8dba51d plane details:  [u'4BA9EB', 30.4896, 52.2252, 341, 37975, 390, u'0547', u'F-OISS1', u'A333', u'TC-JOK', 1455843285, u'DXB', u'IST', u'TK761', 0, 0, u'THY761', 0]
    for planeCount in theJSON:
        if '8d' in planeCount:
            print( "plane id: ", planeCount, "ADSHEX: ", theJSON[planeCount][0], "longitude: ", theJSON[planeCount][1], "latitude: ", theJSON[planeCount][2], 
                "altitude: ", theJSON[planeCount][4], "radar: ", theJSON[planeCount][7],"Aircraft: ", theJSON[planeCount][8], "Reg No.", theJSON[planeCount][9], 
                "From: ", theJSON[planeCount][11], "To: ", theJSON[planeCount][12])
    #print "Number of planes flying now: ", planeTotal

# Show Header and Debug Log
def debug(mechBrowser):
	mechBrowser.set_debug_http(True)
	mechBrowser.set_debug_responses(True)
	logging.getLogger('mechanize').setLevel(logging.DEBUG)



if __name__ == "__main__":
    main()