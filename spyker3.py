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
collections = db.stryker
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument('headless')
#options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
doc=collections.find({'Recheck':0}).skip(750).limit(250)
for i in doc:
        url=i['url']
        print(url)
        driver.get(url)
        time.sleep(3)
        try:
            listelements=[]
            joblocation=''
            address1=''
            adress2=''
            jobId=''
            jobType=''
            dateposted=''
            title=driver.find_element_by_xpath('//h1[@id="jdp-title-job-title"]/span[@class="jdp-title-job-title"]').text
            print(title)
            location=driver.find_element_by_xpath('//div[@class="jdp-job-snapshot-card content-card"]/ul').text
            location=str(location).split('\n')
            for i in location:
                    listelements.append(i)
            index=1
            for j in listelements:
                if 'Job ID' in j:
                    jobId=listelements[index]
                    print(listelements[index])
                if 'Date Posted' in j:
                    dateposted=listelements[index]
                    print('datePosted'+listelements[index])
                if 'Location' in j:
                    adress2=listelements[index]
                if  'Employee Type' in j:
                    print('JobType '+listelements[index])
                    jobType=listelements[index]
                index=index+1
            joblocation=adress2
            print('JOB LOCATION IS '+ joblocation)
            jobdescription=driver.find_element_by_xpath('//div[@id="jdp-job-description-section"]').text
            print(jobdescription)
            collections.update_one({'url':url},{'$set':{
                'title':title,
                'jobId':jobId,
                'jobDescriptionString':jobdescription,
                'jobType':jobType,
                'datePosted':dateposted,
                'Recheck':1,
                'salary':'',
                'location':joblocation,
                'validThrough':'',
            }})
            print('updated')
        except:
            print('xpath is different')
            collections.update_one({'url':url},{'$set':{'Recheck':404}})
driver.quit()


