from threading import Thread
import urllib2
import re
import os
#import MySQLdb


# A multithreaded share pull
  
# Chage working directory
direct = "C:\\Python2.7\\PythonWebScraping\\7_MultiThread"
os.chdir(direct)

# Stringify words
symbolsList = open("ASX_Top100.txt").read()  
symbolsList = symbolsList.split("\n")

print symbolsList

def thread(shareCode):
    pageUrl = "https://au.finance.yahoo.com/q?s=" + shareCode + ".AX"
    htmlfile = urllib2.urlopen(pageUrl)
    htmltext = htmlfile.read()

    regex = '<span id="yfs_l84_'+shareCode.lower()+'.ax">(.+?)</span>'
    pattern = re.compile(regex)
    
    results = re.findall(pattern,htmltext)
    print "the price of " + str(shareCode) + " is " + str(results[0])
    

threadList = []

for symbol in symbolsList:
    print symbol
    target = Thread(target=thread,args=(symbol,))
    target.start()
    threadList.append(target)
    
#Join threads back
for b in threadList:
    b.join()
