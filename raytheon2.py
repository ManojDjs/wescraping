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
    collections = db.raytheon
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    #options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':404}).skip(10).limit(5)
    for i in doc:
        try:
            url=i['url']
            print(url)
            driver.get(url)
            time.sleep(10)
            title=driver.find_element_by_xpath('//h1[@class="ajd_header__job-title"]').text
            print(title)
            jobtype=driver.find_element_by_xpath('//span[@class="job-date job-info"][5]').get_attribute('innerText')
            print(jobtype)
            location=driver.find_element_by_xpath('//p[@class="ajd_header__location"]').text
            print(location)
            jobdescription=driver.find_element_by_xpath('//div[@class="ats-description ajd_job-details__ats-description"]').get_attribute('innerText')
            print(jobdescription)
            collections.update_one({'_id':i['_id']},{'$set':{
                        'Recheck':1,
                        'title':title,
                        'jobId':'',
                        'location':location,
                        'jobDescription':jobdescription,
                        'salary':'',
                        'company':'Raytheon',
                        'validThrough':'',
                        'postedDate':'',
                        'jobType':jobtype
                    }})
        except:
            collections.update_one({'_id':i['_id']},{'$set':{
                    'Recheck':408,
                }})
            print('pages over')
    driver.quit()
    return "DOne"

if __name__ == '__main__':
    app.run(port=3806)

