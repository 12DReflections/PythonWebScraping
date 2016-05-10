import string


#Clean non utf characters from string


## Method 1
invalidString = 'this is a string \xe2\x82\xa1 \xf0\x28\x8c\x28 \xfc\xa1\xa1\xa1\xa1\xa1'
printable = set(string.printable)
cleanstring = filter(lambda x: x in printable, invalidString)
print cleanstring
#http://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python

## Method 2
s = u'Good bye in Swedish is Hej d\xc3'
s = s.encode('ascii',errors='ignore')
print s
