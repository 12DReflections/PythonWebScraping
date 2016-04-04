import urllib2
import lxml.html
import itertools
url = "http://targetstudy.com/school/schools-in-chhattisgarh.html"
req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
stuff = urllib2.urlopen(req).read().encode('ascii', 'ignore')
tree = lxml.html.fromstring(stuff)
print stuff

links = [url]
visited = []
while len(links) > 0:
    # take a link out of the list and mark it as visited
    link = links.pop()
    visited.append(link)

    # open the link and read the contents
    req = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0' })
    stuff = urllib2.urlopen(req).read().encode('utf-8', 'ignore')
    tree = lxml.html.fromstring(stuff)
    print stuff

    # for every link in the page
    for new_link in tree.xpath("(//ul[@class='pagination']/li/a)[last()]/@href"):
        # if link has not been visited yet and is not in the list to visit next
        if new_link not in links and new_link not in visited:
            # add the new link to the list of links to visit
            links.append(new_link)
