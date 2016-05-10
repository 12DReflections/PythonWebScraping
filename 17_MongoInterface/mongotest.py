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



