from pymongo import MongoClient
import time
from selenium import webdriver
import requests
client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
if(client):
   print("connected")
db = client.stage_jobs
collection1 = db.JobLinks_madhu
doc= collection1.find({})
slis=[]
for i in doc:
    lable=i['Label']
    lit=lable.split(' ')
    if len(lit)==1:
        slis.append(lable)
    l= lable.find('job') or lable.find('Job')
    if l!=-1:
         print(lable)
         #collection1.update({'_id':i['_id']},{'$set':{'status':405}})
    fillist=['Sign in','Terms of Use','Website Feedback','Website','feedback','website','About Us','Current Employee Opportunities.',' Opportunities.',
             'Human Resources','Menu Button','join','Join','Alert','Button','Forgot ','Contact Us','Recently ','Company','Posted ',
             'Search','Clear ','Sign In','Login','login','Log In','Visitors','Refer ','Page','>','<','>>','<<','Next','Prev','Previous','bookmark','BookMark',
             'share','Share','careers','Careers','Jobs','listsings','List','list','Home','']
    for word in fillist:
        l=lable.find(word)
        if l != -1:
            print(lable)
            #collection1.update({'_id': i['_id']}, {'$set': {'status': 405}})
    print(slis)




