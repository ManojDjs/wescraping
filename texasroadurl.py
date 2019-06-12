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
url='https://careers.texasroadhouse.com/ListJobs'
driver.get(url)
while True:
    try:
        time.sleep(5)
        link=driver.find_elements_by_xpath('//tbody[@role="rowgroup"]/tr')
        for i in link:
            title=i.find_element_by_xpath('td/a').text
            print(title)
            url=i.find_element_by_xpath('td/a').get_attribute('href')
            print(url)
            address1=i.find_element_by_xpath('td[@class="ShortTextField3-cell"]').text
            address2=i.find_element_by_xpath('td[@class="ShortTextField4-cell"]').text
            location=address1+' '+address2
            print(location)
            if url not in urlsarray :
                d={}
                print(url)
                d['title']=title
                d['url']=url
                d['location']=location
                d['company']='Texas Roadhouse'
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
        try:
          driver.find_element_by_xpath("//span[contains(text(), 'arrow-e')]").click()
        except:
            driver.find_element_by_xpath('//a[@class="k-link k-pager-nav"]/span').click()
    except:break
