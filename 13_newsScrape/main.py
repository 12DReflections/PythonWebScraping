import gethtml
import articleText

def main():
	url = "http://www.theage.com.au/world/us-election/donald-trump-talks-and-talks-and-beneath-the-verbal-deluge-themes-emerge-20160325-gnreo1.html"
	url2 = "http://allrecipes.com.au"
	
	# Get top ranked words from article body <p>, print the keywords
#	article = articleText.getArticle(url)
#	print articleText.getKeywords(article)
	
	# Get top ranked words from a url
	article = gethtml.getHtmlText(url2)
	print articleText.getKeywords(article)


if __name__ == "__main__":
	main()
