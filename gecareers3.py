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
collections = db.gecareers
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
#options.add_argument('headless')
#options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
doc=collections.find({'Recheck':1},no_cursor_timeout=True).skip(500).limit(500)
url=''
for i in doc:
        try:
            url=i['Link']
            id=i['_id']
            print(url)
            driver.get(url)
            time.sleep(5)
            listone=driver.find_element_by_xpath('//div[@class="job-other-info"]/span').text
            print(listone)
            collections.update_one({'_id':id},{'$set':{
                'company':listone,
                'Recheck':2,
            }})
            print('updated')
        except:
            print('xpath is different')
            collections.update_one({'Link':url},{'$set':{'Recheck':404}})
driver.quit()


