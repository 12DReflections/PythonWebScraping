import urllib
import re

#Respone text from query to Google Finance
htmltext = urllib.urlopen("https://www.google.com/finance?q=anz").read()

# (.+?) Dot matches any char except newline, ?
# [^.]* Any string of any chars, repeated any number of times 
regex = '<span id="ref_675233_l">(.+?)</span>'

pattern = re.compile(regex)
results = re.findall(pattern, htmltext) #search the html text for a string matching this pattern

print results
