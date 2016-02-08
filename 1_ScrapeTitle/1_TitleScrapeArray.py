#Scrape the <title> of website from a url array

import urllib #can read online content
import re

urls = ["http://youtube.com", "http://google.com", "http://www.nytimes.com/", "http://edition.cnn.com/"]
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex) #converts and compiles regex for re library

while i < len(urls): 
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern,htmltext)
    
    print(titles)
    i += 1
