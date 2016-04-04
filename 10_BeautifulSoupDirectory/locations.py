#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

file = open ('locations', 'w')

def getLocations(state):	
	url = 'http://www.bom.gov.au/' + state + '/observations/' + state + 'all.shtml'
	page = urllib2.urlopen(url)

	soup = BeautifulSoup(page, "html.parser")

	for tag in soup.find_all('a'):

		path = tag.get('href')
		if path.find('products') > 0:	
			location = tag.contents[0]
			file.write(location + ':' + path + '.txt\n')


states = ['vic', 'nsw', 'tas', 'wa', 'sa', 'nt', 'qld', 'ant']

for state in states:
	getLocations(state)	


	
