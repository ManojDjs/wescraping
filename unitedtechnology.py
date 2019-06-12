import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.sanofi
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'images': 2,}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url = 'https://jobs.utc.com/search-jobs/united%20states?orgIds=1566-23744&kt=1'
urlsarray=[]
driver.get(url)
p=1
while True:
    try:
        driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(p)
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
        time.sleep(5)
        link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
        for i in link:
                url=i.get_attribute('href')
                title=i.text
                print(title)
                print(url)
                d={}
                d['title']=title
                d['url']=url
                d['company']="United technologies"
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
        p=p+1
    except:break

