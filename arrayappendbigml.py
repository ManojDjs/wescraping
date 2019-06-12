import json
import re
import urllib

import requests
from pymongo import MongoClient
import requests
from pymongo import MongoClient
from flask import Flask, redirect, url_for, request
from requests.utils import requote_uri
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app = Flask(__name__)
if (1 == 1):
    dbname = "SAP"
    # db connection for pymongo and jobiak server db
    mongoUrl = 'mongodb://localhost:27017/basics'
    client = MongoClient(mongoUrl)
    collection = client[dbname]['SAPRESPONSE']
    doc=collection.find({'response':'YES'}).skip(0).limit(2000)
    for i in doc:
        try:
            for s in (i['jobdescription']):
                textstring=''.join(s)
                print(textstring)
            collection.update_one({'_id':i['_id']},{'$set':{'Desc':textstring}})
        except:
            print('no description')
