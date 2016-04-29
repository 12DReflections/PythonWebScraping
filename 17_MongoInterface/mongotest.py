import json
from datetime import date, timedelta
from pymongo import MongoClient

#Connect to Mongo Client 
client = MongoClient('mongoURI')
db = client.pyinformatics #define database used
collection = db.first_collection
posts = db.posts
post = {'author': 'julian', 'text': 'hello'}
id_pyinformatics = posts.insert(post)
print 'create the id: %s'%post
client.close()



'''
Clean non utf
import string
#Clean non utf characters
#http://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python
      #clean non UTF from string
        printable = set(string.printable)
        cleanstring = filter(lambda x: x in printable, info['companyName'])

'''
