import threading
import urllib3
from pymongo import MongoClient
import datetime
urllib3.disable_warnings()
import urllib
import requests
from pymongo import MongoClient
import time
import re
import json
client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
if(client):
    print("connected")
db = client.stage_jobs
collections = db.project
collections2=db.company
def getSalary1():
    checker=collections.find({'Recheck':2}).skip(60)
    for i in checker:
        title=i['title']
        print(title)
        id=i['_id']
        try:
           headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               }
           data = {
                       "title":title
                   }
           response = requests.post('http://testapi.jobiak.ai:8101/getSalary', headers=headers, data=data).json()
           if(response['status']==True):
               salary=response['data']
               salary=salary.lstrip().rstrip()
               print(salary)
               collections.update_one({'_id':id},{'$set':{'salary':salary,'setSalary':1,'Recheck':3}})
               print('update')
           else:
               print('slaary no defined')
               collections.update({'_id':id},{'$set':{'setSalary':2}})
        except Exception as findError:
           #collections.update_one({'titles':title},{'$set':{'setSalary':2}})
           print(findError)
def getSalary2():
    checker=collections.find({'Recheck':2}).skip(80)
    for i in checker:
        title=i['title']
        print(title)
        id=i['_id']
        try:
           headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               }
           data = {
                       "title":title
                   }
           response = requests.post('http://testapi.jobiak.ai:8101/getSalary', headers=headers, data=data).json()
           if(response['status']==True):
               salary=response['data']
               salary=salary.lstrip().rstrip()
               print(salary)
               collections.update_one({'_id':id},{'$set':{'salary':salary,'setSalary':1,'Recheck':3}})
               print('update')
           else:
               print('slaary no defined')
               collections.update({'_id':id},{'$set':{'setSalary':2}})
        except Exception as findError:
           #collections.update_one({'titles':title},{'$set':{'setSalary':2}})
           print(findError)
def getSalary3():
    checker=collections.find({'Recheck':2}).skip(1000)
    for i in checker:
        title=i['title']
        print(title)
        id=i['_id']
        try:
           headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               }
           data = {
                       "title":title
                   }
           response = requests.post('http://testapi.jobiak.ai:8101/getSalary', headers=headers, data=data).json()
           if(response['status']==True):
               salary=response['data']
               salary=salary.lstrip().rstrip()
               print(salary)
               collections.update_one({'_id':id},{'$set':{'salary':salary,'setSalary':1,'Recheck':3}})
               print('update')
           else:
               print('slaary no defined')
               collections.update({'_id':id},{'$set':{'setSalary':2}})
        except Exception as findError:
           #collections.update_one({'titles':title},{'$set':{'setSalary':2}})
           print(findError)

t1=threading.Thread(target=getSalary1())
t2=threading.Thread(target=getSalary2())
t3=threading.Thread(target=getSalary3())
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
