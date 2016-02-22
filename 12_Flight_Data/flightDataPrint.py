import json
import urllib2
import mechanize
import logging
from mechanize import Browser
import re
import MySQLdb

# Pull flight data from web
# Source:		https://www.flightradar24.com/60.8,84.57/2
# Direct Link:	https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&

# trial 'http://www.bloomberg.com/markets/api/bulk-time-series/price/AAPL:US?timeFrame=1_DAY'

def main():
	# Set up Mechanize Browser to hide the browser
	ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
	mechBrowser = Browser()
	mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
	
    # Select the website
	feed = mechBrowser.open('https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&').read()
	theJSON = json.loads(feed)
    	
    	printJSON(theJSON) # Bug in JSON library causing indentation error

    #conn = MySQLdb.connect(host=localhost, user=root, passwd=whobutJ90, db=flight_data)




def printJSON(theJSON):
    planeTotal = theJSON["full_count"]
    
    strJSON = json.dumps(theJSON)   # A string version of the JSON to test the regular expression
    regex = ', "(8[\w]{6})": \['         #Regex pattern
    pattern = re.compile(regex)
    planeID = re.findall(pattern, strJSON)

    for planeID in theJSON:
        if '8' in planeID:
            print( "plane id: ", planeID, "ADSHEX: ", theJSON[planeID][0], "longitude: ", theJSON[planeID][1], "latitude: ", theJSON[planeID][2], 
                "altitude: ", theJSON[planeID][4], "radarID: ", theJSON[planeID][7],"Aircraft: ", theJSON[planeID][8], "Reg No.", theJSON[planeID][9], 
                "From: ", theJSON[planeID][11], "To: ", theJSON[planeID][12])




if __name__ == "__main__":
    main()