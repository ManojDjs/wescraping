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
    collection = client[dbname]['AP2']
    doc=collection.find({})
    l=doc.count()
    i=0
    while i<l:
        print("""" four """)
        prev=i
        next=i+4
        i=next
        print(prev)
        print(next)
        doc2= collection.find({}).skip(prev).limit(4)
        for d in doc2:
            print(d)
