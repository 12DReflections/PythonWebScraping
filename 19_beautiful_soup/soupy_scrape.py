from bs4 import BeautifulSoup
from urllib2 import urlopen

# Beautiful Soup Module Runthrough

# Open web page into a string
html = urlopen('https://litemind.com/best-famous-quotes/').read()

soup = BeautifulSoup(html, "lxml")

# Obtain div content without tags
for section in soup.findAll('div', {'class': 'wp_quotepage'}):
	# With Tags
	# print section
	quote = section.findChildren()[0].renderContents()
	author = section.findChildren()[1].renderContents()
	print quote
	print author
	break

# Obtain Whole Page Content
# Search for div, inside dictionary
#print soup.findAll('div', {'class': 'wp_quotepage_quote'})


'''
# Obtain First Item
for section in soup.findAll('div', {'class': 'wp_quotepage'}):
	# With Tags
	# print section
	quote = section.findChildren()[0]
	author = section.findChildren()[1]
	print quote
	print author
	break
'''