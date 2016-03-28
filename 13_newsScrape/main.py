import gethtml
import articleText


# Scrapes a site's context
# Come up with keywords of that site
# Keywords compare to a list of regular words which are removed

def main():
	url = "http://www.theage.com.au/world/us-election/donald-trump-talks-and-talks-and-beneath-the-verbal-deluge-themes-emerge-20160325-gnreo1.html"
	url2 = "http://allrecipes.com.au"
	
	# Get top ranked words from article body <p>, print the keywords
	article = articleText.getArticle(url)
	print article
#	print articleText.getKeywords(article)
	
	# Get htmlText and print the top keywords from a page's text
	article = gethtml.getHtmlText(url)
	keywordsList = articleText.getKeywords(article)
	for keyword in keywordsList[0:10]:
		print keyword

if __name__ == "__main__":
	main()
