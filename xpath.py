import threading
import urllib3
from pymongo import MongoClient
import datetime
urllib3.disable_warnings()
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import time
import re
import json
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.JUNE5
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
page=1
urlsarray=[]
while page<150:
    url='https://jobs.etalentnetwork.com/jobs?page_size=10&page_number='+str(page)+'&sort_by=start_date&sort_order=DESC'
    driver.get(url)
    time.sleep(3)
    page=page+1
    link=driver.find_elements_by_xpath('//a[@class="item-title"]')
    print('uptothisdone')
    print(link)
    for i in link:
        url=i.get_attribute('href')
        title=i.text
        print(title)
        print(url)
        if url not in urlsarray and len(urlsarray)<200:
            d={}
            print(url)
            d['title']=title
            d['url']=url
            collections.insert_one({'Link':url,'Label':title})
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
