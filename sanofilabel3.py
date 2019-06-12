import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
from flask import Flask, jsonify
import requests
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/basics")
if(client):
 print("connected")
db = client.JOBS
collections = db.cpr
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument('headless')
#options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
doc=collections.find({'Recheck':0})
for i in doc:
    url=i['url']
    print(url)
    driver.get(url)
    time.sleep(3)
    try:
        joblocation=''
        address1=''
        adress2=''
        jobId=''
        jobType=''
        company=''
        listelements=driver.find_element_by_xpath('//span[@class="jobdescription"]').text
        print(listelements)
        listelements2=listelements.split('\n')
        print(listelements2)
        index=0
        for j in list(listelements2):
            if 'Req ID' in j:
                jobId=listelements2[index]
                print(listelements2[index])
            if 'Job Type' in j:
                jobType=listelements2[index]
                print('jobType'+listelements2[index])
            index=index+1
        jobdescription=driver.find_element_by_xpath('//div[@class="joblayouttoken displayDTM"][2]').text
        print(jobdescription)
        collections.update_one({'url':url},{'$set':{
            'jobId':jobId,
            'jobDescriptionString':jobdescription,
            'jobType':jobType,
            'Recheck':1,
            'salary':'',
            'validThrough':'',
        }})
        print('updated')
    except:
        print('xpath is different')
        collections.update_one({'url':url},{'$set':{'Recheck':404}})
driver.quit()


