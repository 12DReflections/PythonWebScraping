import urllib2
from bs4 import BeautifulSoup
import urlparse
import mechanize

# Open Browser with mechanize, to view site through browser

def main():
	url = "http://www.junlinmassage.com/"
	mechBrowser = mechanize.Browser()

	mechBrowser.open(url)

	
	for link in mechBrowser.links():
		# print "The base url is: " + link.base_url
		# Correct directory output
		newURL = urlparse.urljoin(link.base_url,link.url)
		print newURL

if __name__ == "__main__":
    main()
