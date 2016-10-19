import mechanize
import urllib2
import time
import random

#### Add Different User Agent Strings
#http://www.useragentstring.com/pages/useragentstring.php?name=Chrome


def main():

	url = "http://www.theage.com.au"
	
	browser = create_browser()
	header = rand_agent_header()
	# Perform the request. You can replace None with the needed data if it's a POST request
	request = urllib2.Request(url, None, header)

	# Open the response of the web page
	response = browser.open(request)

	print response.read()
#	print response.geturl()
	response.close()



def rand_agent_header():
	# Random agent from the list of User Agents
	agents = ['Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.', 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.3', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.3', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.3', 'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.3']
	# Setup your header at a random agent
	header = {'User-Agent': '\'' + agents[random.randint(0, len(agents)-1)] + '\'' }
	return header

def create_browser():
	# With referrer website example
#	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36', 'Referer': 'http://whateveritis.com'}
	# Set up machanize
	browser = mechanize.Browser() 		#Constructor
	browser.set_handle_robots(False) 	#Set robots.txt to false
	return browser

if __name__ == "__main__":
	main()


