import gethtml
import articleText

def main():
	url = "http://www.bbc.com/news/world-australia-35888091"

	# Get the article body
	article = articleText.getArticle(url)

	# Print the keywords
	print articleText.getKeywords(article)

if __name__ == "__main__":
	main()
