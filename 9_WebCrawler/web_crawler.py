import urllib2
from bs4 import BeautifulSoup
import urlparse
import os

#direct = "C:\PythonPrograms\PythonWebScraping\9_WebCrawler\web_crawler.py"
direct = "C:\PythonPrograms\PythonWebScraping\9_WebCrawler"

os.chdir(direct)

htmltext = urllib2.urlopen("http://www.google.com")
