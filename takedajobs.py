import time
from selenium import webdriver
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.takeda
doc=collections.find({})
urlsarray=[]
for element in doc:
    objects=element['title']
    titleandlocation=objects.split('\n')
    print(titleandlocation)
    title=titleandlocation[0]
    location=titleandlocation[1]
    joburl=element['joburl']
    d={}
    d['title']=title
    d['location']=location
    d['url']=joburl
    d['comapany']="Take da jobs"
    urlsarray.append(d)
print(len(urlsarray))
print(urlsarray)

