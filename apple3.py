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
    collections = db.apple
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    #options.add_argument('headless')
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    urlsarray=[]
    doc=collections.find({'Recheck':0}).skip(100).limit(50)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            time.sleep(15)
            jobid=driver.find_element_by_xpath('//div[@class="sum-info"]/div/strong').text
            print(jobid)
            location=driver.find_element_by_xpath('//div[@id="job-location-name"]').text
            print(location)
            jobdescription=driver.find_element_by_xpath('//div[@itemprop="description"]').text
            print(jobdescription)
            collections.update_one({'_id':i['_id']},{'$set':{
                    'location':location,
                    'jobId':jobid,
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
    app.run(port=3802)

