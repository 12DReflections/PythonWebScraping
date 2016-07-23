import json
from datetime import date, timedelta
from pymongo import MongoClient

# Current date
today = str(date.today())

#Connect to Mongo Client 
client = MongoClient('mongoURI')
db = client.pyinformatics #define database used
collection = db.first_collection
posts = db.posts
post = {'date_index' : today, 'data': { 'author': 'julian', 'text': 'hello'}}
id_pyinformatics = posts.insert(post)
print 'create the id: %s'%post
client.close()



