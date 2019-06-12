import time
from selenium import webdriver
import os
import threading
from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/')
def success():
    client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
    if(client):
       print("connected")
    db = client.stage_jobs
    collections = db['00labels']
    collections1 = db['xpaths']
    options = webdriver.ChromeOptions()
    preferences = {'profile.default_content_setting_values': {'images': 2}}
    options.add_experimental_option('prefs', preferences)
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
    doc=collections.find({'Recheck':0}).limit(50)
    for singleLink in doc:
        try:
           print("Into 1st level FOR  "+singleLink['company'])
           compxpath=collections1.find_one({'company':singleLink['company']})
           if(len(compxpath)):
               print("got paths")
               url=singleLink['Link']
               _id=singleLink['_id']
               print(url)
               driver.get(url)
               time.sleep(3)
               if(str(compxpath['descxpath']) != '0'):
                   descxpath1 = str(compxpath['descxpath'])
                   print(descxpath1)
                   print('getting desc.............')
                   desc = driver.find_element_by_xpath(descxpath1).text
                   print(desc)
                   collections.update_one({'_id':singleLink['_id']},{'$set':{'jobDescriptionString':desc}})
                   print('updated')
               if(str(compxpath['jobidxpath'])!= '0'):
                   jobidxpath1 = str(compxpath['jobidxpath'])
                   print('getting job id.............')
                   jobId = driver.find_element_by_xpath(jobidxpath1).text
                   print(jobId)
                   collections.update_one({'_id':singleLink['_id']},{'$set':{'jobId':jobId}})
               if(str(compxpath['locationxpath'])!= '0'):
                   locationxpath1 = str(compxpath['locationxpath'])
                   print('getting location...........')
                   location = driver.find_element_by_xpath(locationxpath1).text
                   print(location)
                   collections.update_one({'_id':singleLink['_id']},{'$set':{'location':location}})
               if(str(compxpath['jobtypexpath'])!= '0'):
                   jobtypexpath1 = str(compxpath['jobtypexpath'])
                   print('getting jobtype.............')
                   jobtype = driver.find_element_by_xpath(jobtypexpath1).text
                   print(jobtype)
                   collections.update_one({'_id':singleLink['_id']},{'$set':{'jobType':jobtype}})
               if(str(compxpath['datepostedxpath'])!= '0'):
                   datepostedxpath1 = str(compxpath['datepostedxpath'])
                   print('getting datposted.............')
                   dateposted = driver.find_element_by_xpath(datepostedxpath1).text
                   print(dateposted)
                   collections.update_one({'_id':singleLink['_id']},{'$set':{'postedDate':dateposted}})
               collections.update_one({'_id':singleLink['_id']},{'$set':{'Recheck':1}})
        except Exception as err:
            print(err)
            collections.update_one({'_id':singleLink['_id']},{'$set':{'Recheck':404}})
    driver.quit()
    return "DOne"
if __name__ == '__main__':
   app.run(port=3817)
Collaps
