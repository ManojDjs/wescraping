import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
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
    collections = db.compass
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    options.add_argument('headless')
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    urlsarray=[]
    doc=collections.find({'Recheck':0}).skip(60).limit(20)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            time.sleep(5)
            location=driver.find_element_by_xpath('//article[@class="main-description-body"]/ul/li[2]').text
            print(location)
            jobdescription=driver.find_element_by_xpath('//article[@class="main-description-body"]').text
            print(jobdescription)
            collections.update_one({'_id':i['_id']},{'$set':{
                    'location':location,
                    'jobId':'',
                    'Recheck':1,
                    'jobDescription':jobdescription,
                    'salary':'',
                    'validThrough':'',
                    'jobType':'',
                    'postedDate':''
                }})
            print('updated')
        except:
               collections.update_one({'_id':i['_id']},{'$set':{'Recheck':404, }})
    driver.quit()
    return "DOne"

if __name__ == '__main__':
    app.run(port=3806)

