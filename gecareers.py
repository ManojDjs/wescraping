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
#options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
urlsarray=[]
page=500
while page<4700:
    try:
        url='https://jobs.gecareers.com/global/en/search-results?from='+str(page)+'&s=1'
        driver.get(url)
        print(page)
        page=page+10
        time.sleep(10)
        link=driver.find_elements_by_xpath('//li[@class="jobs-list-item"]/div[@class="information"]')
        for i in link:
            url=i.find_element_by_xpath('span/a').get_attribute('href')
            title=i.find_element_by_xpath('span/a').text
            print(url)
            print(title)
            dateposted=i.find_element_by_xpath('p[@class="job-info"]/span/span[@class="job-postdate"]').text
            print(dateposted)
            location=i.find_element_by_xpath('p[@class="job-info"]/span/span[@class="job-location"]').text
            print(location)
            d={}
            d['title']=title
            d['location']=location
            d['url']=url
            d['company']="Ge careers"
            d['datePosted']=dateposted
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
    except:
        page=page+10
