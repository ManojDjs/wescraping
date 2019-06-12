import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymongo
import re
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.VR1
collections2=db.VR4
doc=collections2.find({})
l=0
for i in doc:
        if i['Jobs']!=None:
            print(i['Jobs'])
            l=l+1
            print(l)
            collections.insert_one({'Url':i['Jobs'],"Status":1})

