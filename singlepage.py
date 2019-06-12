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
urlsarray=[]
url='https://avacend-openhire.silkroad.com/epostings/index.cfm?fuseaction=app.allpositions&company_id=17287&version=1'
driver.get(url)
time.sleep(10)
while True:
    try:
        link=driver.find_elements_by_xpath('//a[@class="cssAllJobListPositionHref"]')
        for j in link:
            url2=j.get_attribute('href')
            if url2 is None:
                print('no url')
            else:
                d={}
                d['url']=url2
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
                if len(urlsarray)>140:
                    print('jobes exceeded ')
                    quit()
    except:
        break
