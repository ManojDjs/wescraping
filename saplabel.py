import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.takeda
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
while True:
    try:
        url='https://jobs.sap.com/job/South-San-Francisco-HCM-Transformation-and-Planning-Manager-Job-CA-94080/513887401/'
        driver.get(url)
        jobdescription=driver.find_element_by_xpath('//span[@class="jobdescription"]').text
        print(jobdescription)
    except:
        break
