from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
        print("connected")
db = client.JOBS
collections = db.mayoclinic


for x in collections.find({'Recheck':1}):
 #print(x['location'].replace('LOCATION:',''))
 print(x['url'].split('-'))
 first=x['url'].split('-')
 for i in first:
     str(i)
     if i.endswith('br'):
         sec=i.split('b')
         print(sec)
         jobId=sec[0]
         print(jobId)
 print('===================================================')
 collections.update_one({'_id':x['_id']},{'$set':{ 'jobId':jobId }})
