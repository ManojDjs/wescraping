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

page=0
while True:
    try:
        url='https://jobs.sheetz.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=10&startrow='+str(page)
        driver.get(url)
        page=page+1
        time.sleep(3)
        link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
        for i in link:
            title=i.find_element_by_xpath('td[@class="colTitle"]/span/a').text
            print(title)
            url=i.find_element_by_xpath('td[@class="colTitle"]/span/a').get_attribute('href')
            print(url)
            location=''
            street=i.find_element_by_xpath('td[@class="colDepartment hidden-phone"]/span').text
            area=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
            location=street+'  '+area
            print(location)
            jobTYpe=i.find_element_by_xpath('td[@class="colShifttype hidden-phone"]/span').text
            print(jobTYpe)

    except:
        break
