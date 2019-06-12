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
url = 'https://jobs.aus.com/search-jobs?fl=6252001,4566966,6251999'
urlsarray=[]
driver.get(url)
for i in range(1,147):
    driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
    driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
    driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
    time.sleep(5)
    link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
    for i in link:
            url=i.get_attribute('href')
            title=i.find_element_by_xpath('h2').text
            print(title)
            print(url)
            location=i.find_element_by_xpath('span[@class="job-location"]').text
            print(location)
            jobid=i.find_element_by_xpath('span[@class="job-id"]').text
            d={}
            d['title']=title
            d['location']=location
            d['url']=url
            d['company']='Allied Universal'
            d['jobId']=jobid
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
print(urlsarray)
print(len(urlsarray))
driver.quit()
