from threading import Thread
import urllib2
import re
import os
import MySQLdb

# Write to MySQLdb
# Input stock symbol from file, pull value from web,
# Write symbol + value to DB as a Single Query from a Multithread Scrape

# Chage working directory
direct = "C:\PythonPrograms\\8_MultiThreadDB\\" #Change working directory
os.chdir(direct)


gmap = {} #hashmap

def thread(shareCode):
    pageUrl = "https://au.finance.yahoo.com/q?s=" + shareCode + ".AX"
    htmlfile = urllib2.urlopen(pageUrl)
    htmltext = htmlfile.read()

    regex = '<span id="yfs_l84_'+shareCode.lower()+'.ax">(.+?)</span>'
    pattern = re.compile(regex)
    
    results = re.findall(pattern,htmltext)

    try:
        gmap[shareCode] = results[0]
    except:
        print "gmap error"

threadList = []

# Stringify words
symbolsList = open("ASX_Top100.txt").read()  
symbolsList = symbolsList.split("\n")

#Add symbols onto the list of thread symbols.
for symbol in symbolsList:
    print symbol
    target = Thread(target=thread,args=(symbol,))
    target.start()
    threadList.append(target)
    
#Join threads back
for b in threadList:
    b.join()  


# Read DB info from file
login_info = open("C:\PythonPrograms\\8_MultiThreadDB\\dbLogin.txt").read()
login_info = login_info.split()
host = login_info[0]
user = login_info[1]
password = login_info[2]
db = login_info[3]

conn = MySQLdb.connect(host=login_info[0], user=login_info[1], passwd=login_info[2], db=login_info[3])

# Optimise to single query INSERT to MySQL
query = "INSERT INTO stock_table (symbol,last) VALUES "
for key in gmap.keys():
    print 'Insert Values: ', key, gmap[key] #symbol and price
    query = query + "('" + key + "',"+ gmap[key] +")," 
if query.endswith(','):
    query = query[:-1]
    query = query + ';'    
print 'Insert Query: ' + query
x = conn.cursor()
x.execute(query)
conn.commit()
row = x.fetchall()

