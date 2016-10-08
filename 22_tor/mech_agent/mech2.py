import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

# Step find the urls to visit on a webpage

url = "http://franchisecentral.com.au/pb-lawyer/"
br = mechanize.Browser()
urls = [url]
visited = [url]

br.open(urls[0])

for link in br.links():
    newurl = urlparse.urljoin(link.base_url,link.url)
    b1 = urlparse.urlparse(newurl).hostname
    b2 = urlparse.urlparse(newurl).path
    newurl =  "http://"+b1+b2

    if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
        urls.append(newurl)
        visited.append(newurl)
        print newurl

    
print visited
