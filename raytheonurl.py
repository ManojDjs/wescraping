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
url='https://jobs.raytheon.com/search-jobs'
driver.get(url)
while True:
    try:
        time.sleep(10)
        link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li')
        for i in link:
            url=i.find_element_by_xpath('a').get_attribute('href')
            print(url)
            title=i.find_element_by_xpath('a/h2').text
            print(title)
            location=i.find_element_by_xpath('a/span[@class="job-location"]').text
            print(location)
            if url not in urlsarray :
                d={}
                print(url)
                d['title']=title
                d['url']=url
                d['location']=location
                d['company']=' Raytheon'
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
        driver.find_element_by_xpath("//a[contains(text(), 'next')]").click()
    except:
            driver.find_element_by_xpath('//div[@class="pagination-paging"]/a[@class="next"]').click()
