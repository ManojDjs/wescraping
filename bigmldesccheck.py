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
    dbname = "Appcast"
    # db connection for pymongo and jobiak server db
    mongoUrl = 'mongodb://localhost:27017/basics'
    client = MongoClient(mongoUrl)
    collection1 = client[dbname]['BIGML_DATA']
    collection2=client[dbname]['DESCRIPTION_UPDATE']
    doc=collection2.find({'Comments':1})

    for i in doc:
        try:
            print(i['Link'])
            print(i['Comments'])
            print("into ")
            collection1.update_one({'Link':i['Link']},{'$set':{'JOBDESCRIPTION':i['Description'],'RecheckStatus':1}})
            collection2.update_one({'Link':i['Link']},{'$set':{'Status':1}})
        except Exception as findError:
            print(findError)
            #print
