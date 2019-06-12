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
    collection2=client[dbname]['AP2RESPONSE']
    doc=collection.find({'check':0}).skip(300).limit(100)
    jobsarray=[]
    for i in doc:
            print(i['Url'])
            urls = []
            urls.append(i['Url'])
            try:
                url = "https://test.jobiak.ai:8443/labels"
                data = {"urls": urls}
                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
                dataset = r.json()
                print(dataset)
                #SINCE IT GIVES ASSOCIATIVE ARRAY
                posteddate=dataset['results'][0]['posted-date']
                company=dataset['results'][0]['company']
                salary=dataset['results'][0]['salary']
                expirationdate=dataset['results'][0]['expiration-date']
                jobid=dataset['results'][0]['job-id']
                location=dataset['results'][0]['location']
                jobtitle=dataset['results'][0]['job-title']
                jobtype=dataset['results'][0]['job-type']
                url=dataset['results'][0][ 'url']
                jobdescription = dataset['results'][0]['job-description']
                for i in jobdescription:
                    description=''.join(i)
                print(posteddate)
                print(company)
                print(salary)
                print(expirationdate)
                print(jobid)
                print(location)
                print(jobtitle)
                print(jobtype)
                print(url)
                print(jobdescription)
                print(description)
                d={}
                d['posteddata']=posteddate
                d['comapany']=company
                d['salary']=salary
                d['expirationdate']=expirationdate
                d['jobid']=jobid
                d['location']=location
                d['title']=jobtitle
                d['jobtype']=jobtype
                d['joburl']=url
                d['jobdescription']=description
                d['response']='YES'
                collection2.insert_one(d)
                jobsarray.append(d)
                collection.update_one({'check':0},{'$set': {"check":1}})
            except:
                d={}
                d['joburl']=i['Url']
                d['response']='NO'
                print('no job')
                collection2.insert_one(d)
                collection.update_one({'check':0},{'$set': {"check":1}})
print(jobsarray)
print(len(jobsarray))
