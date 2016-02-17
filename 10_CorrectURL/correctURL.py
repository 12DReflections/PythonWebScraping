import urllib2
from bs4 import BeautifulSoup
import urlparse

# Remove Site Extensions from directory name
# External sites add to the url on the page

htmltext = urllib2.urlopen("http://www.nytimes.com").read() 
soup = BeautifulSoup(htmltext, "html.parser")

for tag in soup.findAll('a', href=True):
	raw = tag['href']
	b1 = urlparse.urlparse(tag['href']).hostname
	b2 = urlparse.urlparse(tag['href']).path
	newUrl = "http://" + str(b1) + str(b2)
	print newUrl