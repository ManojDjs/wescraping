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
    collections = db.astrazenca
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    options.add_argument('headless')
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':0}).skip(150).limit(50)
    for i in doc:
        try:
            url=i['url']
            print(url)
            print(i['location'])
            driver.get(url)
            time.sleep(5)
            location=driver.find_element_by_xpath('//div[@class="position-location"]').text
            jobIdk=driver.find_element_by_xpath('//span[@class="job-id job-info"]').text
            jobId=jobIdk.split(":")
            jobId=jobId[1]
            jobdescription=driver.find_element_by_xpath('//div[@class="ats-description"]').text
            postedDatek=driver.find_element_by_xpath('//span[@class="job-date job-info"]').text
            postedDate=postedDatek.split(":")
            postedDate=postedDate[1]
            print(jobId)
            print(location)
            print(jobdescription)
            print(postedDate)
            collections.update_one({'_id':i['_id']},{'$set':{
                'location':location,
                'jobId':jobId,
                'Recheck':1,
                'jobDescription':jobdescription,
                'salary':'',
                'validThrough':'',
                'postedDate':postedDate,
                'jobType':''
            }})
            print('updated')
        except:
            collections.update_one({'_id':i['_id']},{'$set':{'Recheck':404, }})
    driver.quit()
    return "DOne"

if __name__ == '__main__':
    app.run(port=3808)
