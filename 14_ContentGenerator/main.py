import nltk
import urllib2
import readability
from bs4 import BeautifulSoup
from readability.readability import Document

import cookielib

import URLMethods

url = "http://www.nbcnews.com/tech/innovation/drone-delivers-package-residential-area-first-time-n545901"

URLString = URLMethods.URLString(url)
#print URLString #prints the URL after opening for read

readabileArticle = Document(URLString).summary()
readableTitle = Document(URLString).short_title()

soup = BeautifulSoup(readabileArticle, "lxml")
final_article = soup.text
links = soup.findAll('img', src=True)

#print final_article.encode('ascii', 'ignore')

print readableTitle
#print readabileArticle


'''
Python readability https://github.com/buriy/python-readability
Installation::

    easy_install readability-lxml
    or
    pip install readability-lxml

Usage::

    from readability.readability import Document
    import urllib
    
    html = urllib.urlopen(url).read()
    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

'''
