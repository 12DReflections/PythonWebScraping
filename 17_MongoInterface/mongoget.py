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

# List Comprehension
#json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]

#To get back from json again as string list
docs = [json.loads(j_doc, object_hook=json_util.object_hook) for j_doc in json_docs]
print docs

print 'kitty'







