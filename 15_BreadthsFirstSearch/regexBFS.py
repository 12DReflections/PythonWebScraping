import urllib
import re
import time
from threading import Thread
import mechanize
# import readability
from bs4 import BeautifulSoup
# from readability.readability import Document
import urlparse
from readability.readability import Document
import urllib




# Scrapes a website through Breadth First Search
def main():
    url = "http://www.vogue.com.au/"
    regex = "(.*)"
    pattern = url + regex
    scrapedUrls = scraper(url, 1, regex, pattern)
    #scrapedUrls = BFSScrape.scraper(url, 1)

    print scrapedUrls

def scraper(root,steps, regexPattern, pattern):
    #Set the Browser
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]

    urls = [root]
    visited = [root]
    counter = 0
    while counter < steps:
        step_url = scrapeStep(urls, regexPattern, br, pattern) #step_url is all url's visited in one step[]
        urls= []
        for u in step_url:
            if u not in visited:
                urls.append(u)
                visited.append(u)
        counter+=1

    return visited

def scrapeStep(root, regexPattern, _br, pattern):
    result_urls = []

    # Regex pattern to match and add to scraper
    regex = re.compile(pattern)

    # If link match regex pattern, add to list of urls
    for url in root:
        try:
            _br.open(url)

            for link in _br.links():
                    newurl =  urlparse.urljoin(link.base_url,link.url)

                    # remove 'if statement' for all result_url's
                    if regex.match(newurl) and newurl not in result_urls: #not sure whether need the 'and'
                        result_urls.append(newurl)
        except:
            print "Couldn't parce specific link, will continue"
    return result_urls






d = {}
threadlist = []

def getReadableArticle(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]

    html = br.open(url).read()

    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

    soup = BeautifulSoup(readable_article)

    final_article = soup.text

    links = soup.findAll('img', src=True)

    title_article = []
    title_article.append(final_article)
    title_article.append(readable_title)
    return title_article





def dungalo(urls):
    article_text =getReadableArticle(urls)[0]
    d[urls] = article_text



def getMultiHtml(urlsList,steps):

    for urls1 in urlsList:
        try:
            t = Thread(target=scraper, args=(urls1,steps,regexPattern, pattern,))
            threadlist.append(t)
            t.start()
        except:
            nnn = True

    for g in threadlist:
        g.join()



'''
url = ['www.theage.com.au/', 'http://www.heraldsun.com.au/']
print getMultiHtml(url,1)
'''


if __name__ == "__main__":
    main()
