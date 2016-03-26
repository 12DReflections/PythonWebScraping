import mechanize


# Read in a page with mechanize
def getHtmlText(url):
    #Set the user agent
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    mechBrowser = mechanize.Browser()
    mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]

    htmltext = mechBrowser.open(url).read()
    return htmltext

# Get the html as a file
def getHtmlFile(url):
    #Set the user agent
    ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
    mechBrowser = mechanize.Browser()
    mechBrowser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]

    htmlFile = mechBrowser.open(url)
    return htmlFile
