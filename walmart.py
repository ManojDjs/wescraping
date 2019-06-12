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
        url = 'https://careers.walmart.com/results?q=&page='+str(page)+'&sort=rank&expand=department,brand,type,rate&jobCareerArea=all'
        driver.get(url)
        time.sleep(3)
        page=page+1
        loc=driver.find_elements_by_xpath('//div[@class="search__results"]/ul/li[@class="search-result job-listing   "]')
        for i in loc:
            title=i.find_element_by_xpath('div/h4/a').text
            url=i.find_element_by_xpath('div/h4/a').get_attribute('href')
            location=i.find_element_by_xpath('div[@class="job-listing__info"]/span[@class="job-listing__location"]').text
            print(title)
            print(url)
            print(location)
            d={}
            d['title']=title
            d['url']=url
            d['company']='walmart'
        print(urlsarray)
    except:break
