from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
        print("connected")
db = client.Appcast
collections = db.JUNE5
count=0
for x in collections.find({}):
     count=count+1
     i=x['Label']#.replace('Title','')
     print(i)
     print(x['Link'])
     print(count)
     ('===================================================')
     #collections.update_one({'_id':x['_id']},{'$set':{ 'Label':i}})
