import urllib2
from bs4 import BeautifulSoup
import urlparse
import os

# Spider Web Crawler Algorithm
# Create que of URLs, visit new URLs, Keep track of URLs
# Retrieve information from Website,
#   use for new Websites with new information 

#direct = "C:\PythonPrograms\PythonWebScraping\9_WebCrawler\"
direct = "C:\PythonPrograms\PythonWebScraping\9_WebCrawler"

os.chdir(direct)

url = "http://www.mileycyrus.com"


urlList = [url]     #Stack of URLs
visitedList = [url] #List of visited URLs

# Add to end of urlList, pop from start
while len(urlList) > 0:
    try:
        htmltext = urllib2.urlopen(urlList[0]).read() # que
    except:
        print "Error ", urlList[0]

    soup = BeautifulSoup(htmltext, "html.parser")
    urlList.pop(0) #pop off first element of array
    print 'Length of urlList: ', len(urlList)
    
    for tag in soup.findAll('a', href = True):
        tag['href'] = urlparse.urljoin(url, tag['href']) #append top level domain if doesn't exist
        if url in tag['href'] and tag['href'] not in visitedList:
            urlList.append(tag['href'])     #temp jobs to be processed
            visitedList.append(tag['href']) #list of visited URLs

print visitedList                             
