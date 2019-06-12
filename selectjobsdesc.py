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
    dbname = "data_cleansing"
    # db connection for pymongo and jobiak server db
    mongoUrl = 'mongodb://localhost:27017/basics'
    client = MongoClient(mongoUrl)
    collection = client[dbname]['SAP']
    print("Connected successfully!!!")
    mydoc = collection.find({}).skip(0).limit(2)
    urlsdata = ['http://jobs.ruhlhomes.com/mcc/ruhl/ruhl-2019117-2665168.htm?utm_source=appcast&ccuid=18872817134&device=desktop&traffic=paid&cpccents=12','http://jobs.ruhlhomes.com/mcc/ruhl/ruhl-2019117-6704542.htm?utm_source=appcast&ccuid=18872818877&device=desktop&traffic=paid&cpccents=12']
    url = "https://test.jobiak.ai:8443/labels"
    print
    data = {"urls": urlsdata}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    dataset = r.json()
    print(dataset)
    #SINCE IT GIVES ASSOCIATIVE ARRAY
    li = dataset['results'][0]['job-description']
    print(li)
    firstdescelement = li[0]
    length = len(li)
    print(firstdescelement)
    lastdescelement = li[length - 1]
    print(lastdescelement)

    """for Element in dataset['results']:
        print(Element['url'])
        r2 = requests.get('http://18.221.95.143:8015/?url='+Element['url'])
        html = r2.content
        print(html)
        tobematcheddesc=html.split()
        print(tobematcheddesc)"""

"""
    url2 = 'http://18.221.95.143:8015/?url='
    PARAMS = {'job': urlsdata}
    print(PARAMS['job'][0])
    print('it is get method one')
    r2 = requests.get(url=url2, params=PARAMS)
    dataset2 = r2.json()
    print(dataset2)"""
# description = dataset2['results'][0]['job-description']
# print(description)
("for LabelsData in dataset['results']:\n"
 "        Description = ''\n"
 "        for Desc in LabelsData[\"job-description\"][0]:\n"
 "            Description = Description + Desc\n"
 "            print(Description)\n"
 "    # collection.update_one({\"_id\": x[\"_id\"]}, {\"$set\": {\"Status\": 2, \"Diffbot_HTML_Desc\": data[0][\"objects\"][0]['html'],\"DiffBot_PlainText\":data[0][\"objects\"][0]['text']}})\n"
 "   ")
