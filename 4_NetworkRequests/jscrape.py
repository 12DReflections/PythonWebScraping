import urllib
import re

#Obtain Stock Price of CBA
#Scraping for the widget, look for expression in the image
htmltext = urllib.urlopen("http://www.asx.com.au/asx/widget/companyInfoWidget.do?searchType=company&code=CBA").read()

regex = '<td>(.+?)</td>'

pattern = re.compile(regex)

results = re.findall(pattern,htmltext)

print results
