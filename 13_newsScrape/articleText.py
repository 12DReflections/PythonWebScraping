from bs4 import BeautifulSoup
import gethtml
import re

# Use mechanize to to convert <p>'s to text and return it via the URL
def getArticle(url):
    htmltext = gethtml.getHtmlText(url)
    return getArticleText(htmltext)

# Scrape all <p> articles
def getArticleText(webText):
    
    articleText = ""    
    soup = BeautifulSoup(webText,  "html.parser")
    for tag in soup.findAll('p'): #for tag in soup.findAll('p', attrs={"itemprop":"itemDescription}):
        try:
            articleText += ' \n' + str(tag.contents[0].decode("utf-8"))
        except:
            continue

    return articleText



# Rank keywords from article, if word not in common word list
#   if not in dict, then add
#   else increment by one
def getKeywords(articletext):
    commonWords  = open("wordRank.txt").read().split('\n')

    wordDict = {}
    wordList = articletext.lower().split()
    for word in wordList:
        if word not in commonWords and word.isalnum():
            if word not in wordDict:
                wordDict[word] = 1
            if word in wordDict:
                wordDict[word] += 1
    topWords = sorted(wordDict.items(), key=lambda(k,v):(v,k), reverse=True)[0:25]
    
    top25Words = []
    for word in topWords:
        top25Words.append(word[0])

    return top25Words