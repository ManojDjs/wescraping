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
preferences = {'profile.default_content_setting_values': {
                            'durable_storage': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')

urlsarray=[]
page=1
while True:
    try:
        url = 'https://careers.dswinc.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=10&startrow='
        driver.get(url)
        time.sleep(3)
        page=page+1
        loc=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
        for i in loc:
            title=i.find_element_by_xpath('td/span/a').text
            url=i.find_element_by_xpath('td/span/a').get_attribute('href')
            location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
            print(title)
            print(url)
            print(location)
            d={}
            d['title']=title
            d['url']=url
            d['company']='DSW'
            print(d)
            urlsarray.append(d)
        print(urlsarray)
    except:break

