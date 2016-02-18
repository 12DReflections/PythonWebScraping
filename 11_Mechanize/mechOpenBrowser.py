import urllib2
from bs4 import BeautifulSoup
import urlparse
import mechanize

# Open Browser with mechanize, to view site through browser

def main():
	url = "http://www.junlinmassage.com/"
	mechBrowser = mechanize.Browser()

	mechBrowser.open(url)

	# Correct directory output
	for link in mechBrowser.links():
		newURL = urlparse.urljoin(link.base_url,link.url)
		b1 = urlparse.urlparse(newURL).hostname
		b2 = urlparse.urlparse(newURL).path
		print "http://" + b1 + b2


'''	
	for link in mechBrowser.links():
		# print "The base url is: " + link.base_url
		# Directory output
		newURL = urlparse.urljoin(link.base_url,link.url)
		print newURL

'''

if __name__ == "__main__":
    main()
