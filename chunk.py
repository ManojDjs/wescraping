import threading
import requests
import urllib3
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime

urllib3.disable_warnings()
import urllib

from pymongo import MongoClient

import requests
from pymongo import MongoClient
from flask import Flask, jsonify

import time

start_time = time.time()
app = Flask(__name__)
import re
import time

start_time = time.time()
import json
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db['manoj']
def success():
        if __name__ == '__main__':
            client = MongoClient("mongodb://localhost:27017/basics")
        if(client):
           print("connected")
        db = client.Appcast
        collections1 = db['manoj']
        mydoc1 = collections1.find({'status': 0}).skip(0)
        for Document1 in mydoc1:
            if(isinstance(Document1['Link'],dict)):
              if('url' in Document1['Link']):
                print(Document1['Link']['url'],Document1['_id'])
                url=Document1['Link']['url']
                print("++++++++++++")
                print(url)
              else:
                print(Document1['Link']['Url'],Document1['_id'])
                url=Document1['Link']['Url']
                print("**************")
                print(url)
                #collections.update_one({Document1['Link']['Url'],Document1['_id']},{'$set':{Document1['Link']:url}})
            else:
                print(Document1['Link'])
                print(Document1['Link'],Document1['_id'])

success()
