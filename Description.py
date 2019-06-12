import pymongo
from difflib import SequenceMatcher
myclient = pymongo.MongoClient('mongodb://jobiak:jobiak@18.223.47.109:28015/data_cleansing')
mydb = myclient['data_cleansing']
mycol = mydb["title_desc_comp_loc"]

x = mycol.aggregate([{'$group': {'_id': {'title':"$title",'company':"$company",'location':"$location"},'count': {'$sum': 1}}},{'$sort': {'count': -1}}])
for data in x:

    dataset=mycol.find({'title':data['_id']['title'],'company':data['_id']['company'],'location':data['_id']['location']})
    Descset=[]
    for data1 in dataset:
        #print(data1['body'])
        Descset.append(data1['body'])
    Avg=[]
    Avgno=0
    for i in range(0,len(Descset)):
        MainDesc=Descset[i]
        for j in range(i+1,len(Descset)):
            print(SequenceMatcher(None, MainDesc, Descset[j]).ratio())
            Avg.append((SequenceMatcher(None, MainDesc, Descset[j]).ratio()*100))
        for Sumdata in Avg:
            Avgno=Avgno+Sumdata
        print(Avgno)
        print("--------------------")
        print(Avgno/len(Avg))
        print("--------------------")
        if ((Avgno/len(Avg))>=80.0):
            print('Best Desc')
            print("----------------------------DONE-----------------------------")
