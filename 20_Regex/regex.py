import re

# Extract regex and remove duplicates from a list

# Remove everything after the hash and clean
search_list = ['http://www.theage.com.au/federal-politics/by/Matthew-Knott-hvf2k?deviceType=text#tab-mostread2', 'http://www.theage.com.au/federal-politics/political-news/it-was-a-human-reaction-malcolm-turnbull-defends-giving-money-to-a-beggar-20160819-gqwbvf.html#nav', 'http://www.theage.com.au/federal-politics/political-news/it-was-a-human-reaction-malcolm-turnbull-defends-giving-money-to-a-beggar-20160819-gqwbvf.html#content', 'http://www.theage.com.au/federal-politics/political-news/it-was-a-human-reaction-malcolm-turnbull-defends-giving-money-to-a-beggar-20160819-gqwbvf.html#footer']

exp = '(.*)#?' # question mark makes it optional
pattern = re.compile(exp)

result = []
for item in search_list:
	cleaned_url = re.findall(pattern, item)
	result.append(cleaned_url[0])

result = list(set(result))
print result