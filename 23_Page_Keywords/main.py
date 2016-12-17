
from bs4 import BeautifulSoup

from urllib2 import urlopen





def main():
	
	mylist = clean_list()
	#print mylist

	website_list = mylist
	
	
	meta_data = title_description_keywords(website_list)
	print meta_data


	# Separate on tab
	data_string = "".join(str(x) + '\t' for x in meta_data)
	print data_string

	column = 0

	for char in data_string:
		if char == '\t':
			column+=1
			if column == 4:
				char = '\n'
				column = 0

	print data_string
# Inputs a list of websites and outputs their site_title_desc_key as a list 
def title_description_keywords(website_list):
	site_title_desc_key = []

	for website in website_list:
	# Open web page into a string
		try:
			html = urlopen(website).read()
			#print html success!
			soup = BeautifulSoup(html, "lxml")
		except: 
			continue
		try:
			# Get the title
			title = soup.title.string
		except: 
			title = " "
			continue

		try: 	
			# Get the description
			html_desc = soup.findAll(attrs={"name":"description"}) 
			description = html_desc[0]['content'].encode('utf-8')
		except:
			description = " "
			continue
		try:
			# Get the keywords
			html_keyword = soup.findAll(attrs={"name":"keywords"}) 
			keyword = html_keyword[0]['content'].encode('utf-8')
		except:
			keywords = " "
			continue		
		# print title
		# print description
		# print keyword

		site_title_desc_key.append(website)
		site_title_desc_key.append(title)
		site_title_desc_key.append(description)
		site_title_desc_key.append(keyword + '\n')
	return site_title_desc_key


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