import urllib2
from bs4 import BeautifulSoup
import urlparse

# Print all web URL's and all directories of site

def main():
	url = "http://cityhealthandmassage.com.au"
	base = "http://cityhealthandmassage.com.au/"

	htmlfile = urllib2.urlopen(url)
	soup = BeautifulSoup(htmlfile, "html.parser")

	for tag in soup.findAll('a', href = True):
		print base + tag['href']
'''
	# Path without hostname
	for tag in soup.findAll('a', href=True):
		print urlparse.urlparse(tag['href']).path
'''

if __name__ == "__main__":
    main()