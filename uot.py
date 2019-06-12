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
page=2
while True:
    try:
        url='https://careers-guardian.icims.com/jobs/search?pr='+str(page)+'&schemaId=&o='
        driver.get(url)
        page=page+1
        time.sleep(5)
        link=driver.find_elements_by_xpath('//div[@class="col-xs-12 title"]/a')
        for i in link:
            url=i.get_attribute('href')
            if url not in urlsarray:
                print(url)
                d={}
                d['url']=url

                if url in urlsarray:
                    print('already innnn')
                else:
                    urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
                if len(urlsarray)>100:
                    print('jobes exceeded ')
                    quit()

    except:
        break
