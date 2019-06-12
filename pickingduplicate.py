from pymongo import MongoClient
import requests
from pymongo import MongoClient
from flask import Flask, redirect, url_for, request
from requests.utils import requote_uri
import time
start_time = time.time()
app = Flask(__name__)
import re

if (1 == 1):
   dbname1 = "stage_jobs"
   mongoUrl1 = 'mongodb://' + 'jobiak' + ':' + 'j0Bi%40kSt%40ge' + '@' + "18.223.47.109" + ':' + str(
       '28015') + '/' + dbname1
   client1 = MongoClient(mongoUrl1)
   collection1 = client1[dbname1]['appCast_Skills_1']
   print("Connected successfully!!!")
   mydoc1 = collection1.find( no_cursor_timeout=True).limit(50)
   titlearray=[]

   for data in mydoc1:
       duplicateid=[]
       duplicatetitle=[]
       titletoematched=data['title']
       print(titletoematched)
       mydoc2=collection1.find({'title':titletoematched})
       for id in mydoc2:
           if id not in duplicateid:
              duplicateid.append(id['_id'])
              duplicatetitle.append(titletoematched)
       print(len(duplicateid))
       headtitle, sep, tail = titletoematched.partition('-')
       print(headtitle)
       titlearray=headtitle.split(" ")
       for elementtosearch in titlearray:
           if elementtosearch in titletoematched and id["_id"] not in duplicateid and headtitle not in duplicatetitle:
               duplicateid.append(id["_id"])
               print("added")
       #print(len(duplicateid))

   print("____________________")
       #collection1.update_one({'_id':data['_id']},{'$set':{'DirectTitleMatchID':duplicateid,'Recheck':202}})


