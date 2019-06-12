import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
import urllib
from flask import Flask, jsonify
import requests
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/')
def success():
    client = MongoClient("mongodb://localhost:27017/basics")
    if(client):
        print("connected")
    db = client.JOBS
    collections = db.texasroad
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':0}).skip(0).limit(5)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            jobdescription=driver.find_element_by_xpath('//div[@class="job-detail-jobdescription"]').text
            print(jobdescription)
            collections.update_one({'_id':i['_id']},{'$set':{
                'Recheck':1,
                'jobId':'',
                'jobDescription':jobdescription,
                'salary':'',
                'validThrough':'',
                'postedDate':'',
                'jobType':''
            }})
            print('updated')
        except:
            collections.update_one({'_id':i['_id']},{'$set':{'Recheck':404, }})
    driver.quit()
    return "DOne"

if __name__ == '__main__':
    app.run(port=3800)