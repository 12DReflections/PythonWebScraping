import urllib
import re
import time
from threading import Thread
#import MySQLdb
import mechanize
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import urlparse




def scraper(root,steps):
    urls = [root]
    visited = [root]
    counter = 0
    while counter < steps:
        step_url = scrapeStep(urls)
        urls= []
        for u in step_url:
            if u not in visited:
                urls.append(u)
                visited.append(u)
        counter+=1           

    print visited     

def scrapeStep(root):
    result_urls = []
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]

    for url in root:
        try:
            br.open(url)
            for link in br.links():
                    newurl =  urlparse.urljoin(link.base_url,link.url)
                    print newurl
                    result_urls.append(newurl)
        except:
            print "error"       
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
            t = Thread(target=scraper, args=(urls1,steps,))
            threadlist.append(t)
            t.start()            
        except:
            nnn = True

    for g in threadlist:
        g.join()


#print getMultitml(url,13)
