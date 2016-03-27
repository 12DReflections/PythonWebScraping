#Christopher Reeves Web Scraping Tutorial
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib 
import mechanize 
from bs4 import BeautifulSoup
import urlparse
import json
import gzip 


def main():
    url = "http://www.nbcnews.com/tech/innovation/drone-delivers-package-residential-area-first-time-n545901"

    translateString()


def translateString(homeLanguage, targetLanguage, transText):
    postUrl = "http://translate.google.com/translate_a/t"
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]

    parameters = { 'client' : 't', 'text' : transText, 'hl': homeLanguage, 'sl' : homeLanguage, 'tl' : targetLanguage, 'ie' : 'UTF-8', 'oe' : 'UTF-8', 'multires' : '1', 'otf' : '2', 'pc' : '0', 'ssel' : '0', 'tsel' : '0'}


    data = urllib2.urlencode(parameters)

    transArray = browser.open(postUrl, data).read().decode('UTF-8')

    transString = ""
    sections = trans_array.split("]]")
    secArray = sections[0].replace("[[[", "").replace("],[", "").replace('""', '/'/'').split('"')

    co = -1
    for thing in secArray:
        if co %6 == 0:
            trans_string += thing
            cp +=1
    print trans_string

if __name__ == "__main__":
    main()