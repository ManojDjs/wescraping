import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
collection = mydb["hyd_glassdoor"]

TitlesDataset = collection.find({'status':0},).limit(100)

for TitleSet in TitlesDataset:
   try:
       Title=TitleSet['job_title']
       print(Title)
       URL="http://localhost:4010/?title="+Title
       r = requests.get(url=URL)
       data = r.json()
       print(data)
       collection.update_one({'_id':TitleSet['_id']},{'$set':{'occupation_category':data['occupation_category'],'LDJSON':data['LdJson'],'status':100}})
   except:
       pass
