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
    mongoUrl = 'mongodb://jobiak:jobiak@18.223.47.109:28015/data_cleansing'
    client = MongoClient(mongoUrl)
    collection = client[dbname]['diffbot']
    print("Connected successfully!!!")
    mydoc = collection.find({}).skip(0)
    urlsdata = []
    for x in mydoc:
        urlsdata.append(x['OriginalUrl'])
    #passing api tho this url gives bigml format html and diffbot prediction
    url = "http://35.167.157.151:8021/?Url="

    for i in urlsdata:
        print(i)
        r = requests.get(url+i)
        dataset = r.json()
        print(dataset)
        bigmldesc = dataset['BigmlDesc_API_Response']['value']
        """for i in range(0, len(bigmldesc)-1):
            print(bigmldesc[i]['content'])"""
        #first line in description
        firstline = bigmldesc[0]['content']
        print('bigml first and last')
        print(firstline)
        lastindex = len(bigmldesc)-1
        lastline = bigmldesc[lastindex]['content']
        print(lastline)
        htmlcontent = dataset['PageHTML']
        def gettinghtmlcontent(htmlcontent):
            pass
        def cleanhtml(raw_html):
           cleanr = re.compile('<.*?>')
           cleantext = re.sub(cleanr,'', raw_html)
           return(cleantext)
        diffbotdesc = dataset['Diffbot'][0]['objects'][0]['html']
        difflist=diffbotdesc.split('\n')
        difffirstelement=difflist[0]
        difflen=len(difflist)-1
        difflastelement=difflist[difflen]
        print('+++++++++++++++++++++++++++++++++++++++++++++++')
        print('***********************************************')
        print('diffbot first and last')
        print(cleanhtml(difffirstelement))
        print(cleanhtml(difflastelement))
        #SINCE IT GIVES ASSOCIATIVE ARRAY
