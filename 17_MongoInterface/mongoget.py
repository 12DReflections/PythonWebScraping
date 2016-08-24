import json
from datetime import date, timedelta
from pymongo import MongoClient
from bson import json_util

#Connect to Mongo Client 
client = MongoClient('user://pword:dreamerthewise@ds047124.mlab.com:47124/politicians_from_theage')
db = client.politicians_from_theage #define database used
print db
# Define Collection
collection = db.posts
print collection # print Collection(Database(MongoClient(host=['ds047124.mlab.com:47124']...


cursor = collection.find()
print cursor

json_docs = []
for doc in cursor:
    json_doc = json.dumps(doc, default=json_util.default)
    json_docs.append(json_doc)




print 'kitty'







