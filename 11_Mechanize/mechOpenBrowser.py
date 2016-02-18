import urllib2
from bs4 import BeautifulSoup
import urlparse
import mechanize


def main():
	url = "http://www.junlinmassage.com/"
	mechBrowser = mechanize.Browser()

	mechBrowser.open(url)

	
	for link in mechBrowser.links():
		print link
		print "The base url is: " + link.base_url
		
if __name__ == "__main__":
    main()
