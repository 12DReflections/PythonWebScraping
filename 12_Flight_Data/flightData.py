import json
import urllib2
import mechanize
from mechanize import Browser
import re
import MySQLdb
import datetime 

# Pull flight data from web
# Source:		https://www.flightradar24.com/60.8,84.57/2
# Direct Link:	https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&

# Mechanize to hide the browser
ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
mechBrowser = Browser()
mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]

# Select the website
feed = mechBrowser.open('https://data.flightradar24.com/zones/fcgi/feed.js?bounds=84.84349829468273,-35.50198011442717,5344.1015625,470.7421875&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=900&gliders=1&stats=1&').read()
theJSON = json.loads(feed)
	
# Pull the regex of planeID's from a string of "theJSON" 
strJSON = json.dumps(theJSON)   # A string version of the JSON to test the regular expression
regex = ', "(8[\w]{6})": \['         #Regex pattern
pattern = re.compile(regex)
planeID = re.findall(pattern, strJSON)
planeTotal = theJSON["full_count"]

# Current date and time for MySQL query
now = datetime.datetime.now()
format = '%Y-%m-%d %H:%M:%S'
nowTime = now.strftime(format)


# MySQL connection and query 
conn = MySQLdb.connect(host='localhost', user='root', passwd='whobutJ90', db='flight_data')
entryCount = 0
query = "INSERT INTO flight_table (planeID,ADSHEX,longitude,latitude,altitude,radarID,aircraft,departing,destination,dateTime) VALUES "
for planeID in theJSON:
        if '8' in planeID or '9' in planeID:
#                                   planeID                 ADSHEX                              long                            lat                             altitude                         radarID                                aircraft                         from                               to                                  currentTime
            query = query + "('" + str(planeID) + "','" + str(theJSON[planeID][0]) + "'," + str(theJSON[planeID][1]) + "," + str(theJSON[planeID][2]) + "," + str(theJSON[planeID][4]) + ",'" + str(theJSON[planeID][7]) + "','" + str(theJSON[planeID][8])  + "','" + str(theJSON[planeID][11]) + "','" + str(theJSON[planeID][12]) + "','" + str(nowTime)  + "')," 
            entryCount += 1
# Replace final comma with semi-colon in the query
if query.endswith(','):
    query = query[:-1]
    query = query + ';' 

x = conn.cursor()
x.execute(query)
conn.commit()
row = x.fetchall()
#print entryCount, ' rows entered successfully'

'''
# Print to flight details to screen
entryCount =0
for planeID in theJSON:
    entryCount +=1
    if '8' in planeID or '9' in planeID:
        print( "plane id: ", planeID, "ADSHEX: ", theJSON[planeID][0], "longitude: ", theJSON[planeID][1], "latitude: ", theJSON[planeID][2], 
            "altitude: ", theJSON[planeID][4], "radarID: ", theJSON[planeID][7],"Aircraft: ", theJSON[planeID][8], "Reg No.", theJSON[planeID][9], 
            "From: ", theJSON[planeID][11], "To: ", theJSON[planeID][12])
        
print entryCount

'''
