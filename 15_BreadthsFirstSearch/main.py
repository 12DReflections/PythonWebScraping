import BFSScrape
import regexBFS

# Scrapes a website 

def main():
        url = "http://www.seek.com.au/"
#        scrapedUrls = BFSScrape.scraper(url, 2)
        scrapedUrls = regexBFS.scraper(url, 1)
        
if __name__ == "__main__":
        main()
