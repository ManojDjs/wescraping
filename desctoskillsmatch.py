import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://jobiak:j0Bi%40kSt%40ge@18.223.47.109:28015/stage_jobs")
if(client):
    print("connected")
db = client.stage_jobs
collections = db.ALL_DICE_FINAL
collections2=db.final_merged_data
doc = collections.find({})
doc2=collections2.find({'Status':100,'SKILL-SET':{'$ne':"set()"}})
count=0
referenceid=[]
for matchedskills in doc2:
    li=(matchedskills['SKILL-SET'])
    for element in doc:
        if li in element['Skill_name']:
            if matchedskills['_id'] not in referenceid:
                referenceid.append(matchedskills['_id'])
                print(matchedskills['_id'])
print(referenceid)



