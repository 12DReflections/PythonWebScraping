
from bs4 import BeautifulSoup
from urllib2 import urlopen
import string

def main():
	
	#Get a list from a text file 
	website_list = clean_list()
	#mylist = ['http://www.cairnsindoorsports.com.au', 'http://www.poleplaystudios.com.au', 'http://www.jennycraig.com.au']
	#print mylist

		
	meta_data = title_description_keywords(website_list)
	#print meta_data
	# #Clean non utf chars
	#print meta_data
	#print 'blue'
	# clean_meta_data = clean_non_utf(meta_data)
 
	# print clean_meta_data
	# print 'orange'
	# Separate on tab

	

	with open("Output7.txt", "w") as text_file:
	    for x in meta_data:
			x = x.encode('ascii',errors='ignore')
			text_file.write("%s0110" % x)

	text_file.close()


	# print data_string
# Inputs a list of websites and outputs their site_title_desc_key as a list 
def title_description_keywords(website_list):
	site_title_desc_key = []

	for website in website_list:
	# Open web page into a string
		print website
		try:
			html = urlopen(website).read()
			#print html success!
			soup = BeautifulSoup(html, "lxml")

			# Append the website
			site_title_desc_key.append(website)
		except:
			print str(website) + " could not load" # Debugging
			continue
		try:
			# Get the title
			title = soup.title.string  + '\t'
		except: 
			title = " x " + '\t'
			continue
		site_title_desc_key.append(title)
		
		try: 	
			# Get the description
			html_desc = soup.findAll(attrs={"name":"description"}) 
			description = html_desc[0]['content'].encode('utf-8')  + '\t'
			
		except:
			description = " x "  + '\t'
			continue
		site_title_desc_key.append(description)

		try:
			# Get the keywords
			html_keyword = soup.findAll(attrs={"name":"keywords"}) 
			keyword = html_keyword[0]['content'].encode('utf-8')  + '\t'
		except:
			keywords = " x "  + '\t'
			continue		
		site_title_desc_key.append(keyword)
		site_title_desc_key.append('\n')

		# print title
		# print description
		# print keyword
	return site_title_desc_key



def clean_non_utf(invalidString):
	for item in invalidString:
		cleanstring = item.encode('ascii',errors='ignore')
	return cleanstring

# Get a File of Strings into a deduplicated list
def clean_list():
	clean_list = []		 	
	website_file = open("company_list.txt")

	symbols_string = website_file.read()
	
	for line in symbols_string.splitlines():
		if line not in clean_list:
			clean_list.append(line)

	return clean_list

if __name__=='__main__':
	main()