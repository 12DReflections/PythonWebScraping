import BFSScrape
import tes4

# Scrapes a website 

def main():
        url = "http://www.careerone.com.au/"
#        scrapedUrls = BFSScrape.scraper(url, 1)
        scrapedUrls = tes4.scraper(url, 3)
        
if __name__ == "__main__":
        main()
