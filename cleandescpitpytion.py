from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
        print("connected")
db = client.JOBS
collections = db.honda
for x in collections.find({'Recheck':1}):
     #print(x['location'].replace('LOCATION:',''))
     title=x['title']
     print(x['jobDescriptionString'].replace(title,''))
     newjobdesc=x['jobDescriptionString'].replace(title,'')
     jobidlist=newjobdesc.split('\n')
     for i in jobidlist[0:5]:
         if 'Job Number' in i:
               print(i)
               print(len(i))
               length=len(i)
               sliceup=i[2:length-1]
               print(sliceup)
               jobidlist2=sliceup.split(':')
               jobid=jobidlist2[1]
               print(jobid)
     print('===================================================')
     collections.update_one({'_id':x['_id']},{'$set':{ 'jobId':jobid,'jobDescriptionString':newjobdesc }})
