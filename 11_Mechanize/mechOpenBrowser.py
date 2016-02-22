import urllib2
from bs4 import BeautifulSoup
import urlparse
import mechanize

# Open Browser with mechanize, to view site through browser

def main():
	url = "http://www.junlinmassage.com/"
	mechBrowser = mechanize.Browser()

	mechBrowser.open(url)
	#debug(mechBrowser) 

	# Correct directory output
	for link in mechBrowser.links():
		newURL = urlparse.urljoin(link.base_url,link.url)
		b1 = urlparse.urlparse(newURL).hostname
		b2 = urlparse.urlparse(newURL).path
		print "http://" + b1 + b2


# Show Header and Debug Log
def debug(mechBrowser):
	mechBrowser.set_debug_http(True)
	mechBrowser.set_debug_responses(True)
	logging.getLogger('mechanize').setLevel(logging.DEBUG)

if __name__ == "__main__":
    main()
