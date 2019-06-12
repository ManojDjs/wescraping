import time
import re
import threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
if(client):
    print("connected")
db = client.stage_jobs
collections = db.project
collections2=db.company
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url='https://jobs.compassgroupcareers.com/search/?searchby=location&createNewAlert=false&q=&locationsearch=&geolocation='
driver.get(url)
#driver.find_element_by_xpath('//a[@class="c-button js-filter-careers"]').click()
time.sleep(3)
while True:
        for i in range(0,3):
                driver.find_element_by_xpath('//button[@id="tile-more-results"]').click()
                print('page is loading')
                time.sleep(2)
        try:
            link=driver.find_elements_by_xpath('//div[@class="col-md-12 sub-section sub-section-desktop hidden-xs hidden-sm"]/div/div/h2/a')
            for i in link:
                time.sleep(1)
                title=i.text
                url=i.get_attribute('href')
                print(title)
                print(url)
                d={}
                d['title']=title
                d['url']=url
                d['company']='Compass Group careers'
                print(d)
                collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Compass Group careers','Recheck':0})
        except:
            break
