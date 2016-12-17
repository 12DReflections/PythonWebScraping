#!/usr/bin/env python
# -*- coding: latin-1 -*-
import urllib2



def translate(to_translate, to_langage="auto", langage="auto"):
	'''Return the translation using google translate
	you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
	if you don't define anything it will detect it or use english by default
	Example:
	print(translate("salut tu vas bien?", "en"))
	hello you alright?'''
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read().decode('utf-8','ignore').encode("utf-8")
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

#Return a UTF String that previous showed decoding error from ASCII
def UTF_Clean(sentence):
	sentenceList = sentence.split(" ")

	UTF_Clean = ''

	for word in sentenceList:
		try:
			UTF_Clean += " " + str(word)
		except:
			continue
	return UTF_Clean


def main():

	with open('text.txt', 'r') as f:
	     to_translate = f.read()
	

	to_translate = translate(to_translate, 'fr')
	to_translate = translate(to_translate, 'es')

	to_translate = translate(to_translate, 'en')


	print(to_translate)

	f = open('output.txt','w')
	f.write(to_translate) # python will convert \n to os.linesep

if __name__ == '__main__':
	main()
	# to_translate = 'Hola como estas?'
	# print("%s >> %s" % (to_translate, translate(to_translate)))
	# print("%s >> %s" % (to_translate, translate(to_translate, 'fr')))
	# #should print Hola como estas >> Hello how are you
	#and Hola como estas? >> Bonjour comment allez-vous?
