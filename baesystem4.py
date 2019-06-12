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
    collections = db.baesystems2
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':0}).skip(30).limit(5)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            time.sleep(10)
            title=driver.find_element_by_xpath('//div[@class="job-info au-target"]/h1').text
            print(title)
            location=driver.find_element_by_xpath('//div[@class="job-info au-target"]/div/span[@show.bind="jobDetail.location"]').text
            print(location)
            jobid=driver.find_element_by_xpath('//div[@class="job-info au-target"]/div/span[@class="job-id au-target"]').text
            print(jobid)
            jobtype=driver.find_element_by_xpath('//div[@class="job-other-info"]/span[@show.bind="jobDetail.fullTimepartTime"]').text
            print(jobtype)
            jobdescription=driver.find_element_by_xpath('//div[@class="jd-info au-target"]').text
            print(jobdescription)
            posteddate=driver.find_element_by_xpath('//span[@show.bind="jobDetail.postedDate"]').text
            print(posteddate)
            collections.update_one({'_id':i['_id']},{'$set':{
                'title':title,
                'location':location,
                'jobId':jobid,
                'Recheck':1,
                'jobDescription':jobdescription,
                'salary':'',
                'validThrough':'',
                'postedDate':posteddate,
                'jobType':jobtype
            }})
            print('updated')
        except:
            collections.update_one({'_id':i['_id']},{'$set':{'Recheck':404, }})
    driver.quit()
    return "DOne"

if __name__ == '__main__':
    app.run(port=3806)
