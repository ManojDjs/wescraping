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
page=0
while True:
    try:
        url='https://careers.checkers.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
        driver.get(url)
        page=page+25
        time.sleep(3)
        link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
        for i in link:
            url=i.find_element_by_xpath('td/span/a').get_attribute('href')
            title=i.find_element_by_xpath('td/span/a').text
            print(title)
            print(url)
            location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
            postedDate=i.find_element_by_xpath('td[@class="colDate hidden-phone"]/span').text
            if url not in urlsarray and len(urlsarray)<1100:
                d={}
                print(url)
                d['title']=title
                d['url']=url
                d['location']=location
                d['company']='Checkers Drive-In Restaurants'
                d['postedDate']=postedDate
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
    except:
        break
