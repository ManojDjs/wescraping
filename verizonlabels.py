import threading
import requests
import urllib3
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime

urllib3.disable_warnings()
import urllib

from pymongo import MongoClient

import requests
from pymongo import MongoClient
from flask import Flask, jsonify

import time
import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
app = Flask(__name__)

@app.route('/')
def success():
    client = MongoClient("mongodb://localhost:27017/basics")
    if(client):
        print("connected")
    db = client.JOBS
    collections = db.verizon
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                                'plugins': 2, 'popups': 2, 'geolocation': 2,
                                'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                'durable_storage': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':0}).limit(10)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            title=driver.find_element_by_xpath('//article[@id="job_title"]/h1').text
            print(title)
            dateposted=driver.find_element_by_xpath('//span[@itemprop="datePosted"]').text
            print(dateposted)
            jobid=driver.find_element_by_xpath('//ul[@class="story-info clear-float"]/li[2]').text
            print(jobid)
            location=driver.find_element_by_xpath('//span[@itemprop="address"]').text
            print(location)
            jobdescription=driver.find_element_by_xpath('//div[@class="cs_item_text"]').get_attribute('innerText')
            print(jobdescription)
            collections.update_one({'_id':i['_id']},{'$set':{
                'Recheck':1,
                'title':title,
                'jobId':jobid,
                'location':location,
                'jobDescription':jobdescription,
                'salary':'',
                'company':'verizon',
                'validThrough':'',
                'postedDate':dateposted,
                'jobType':''
            }})
        except:
            collections.update_one({'_id':i['_id']},{'$set':{'Recheck':404,}})
            pass
    return "DOne"

if __name__ == '__main__':
    app.run(port=3512)
