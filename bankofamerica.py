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
url='https://careers.bankofamerica.com/search-jobs.aspx?c=united-states&r=us'
driver.get(url)
while True:
    try:
        time.sleep(35)
        link=driver.find_elements_by_xpath('//td[@class="jobtitle"]/a')
        for i in link:
            time.sleep(1)
            url=i.get_attribute('href')
            title=i.text
            print(title)
            if url not in urlsarray:
                print(url)
                d={}
                if url in urlsarray:
                    print('already innnn')
                else:
                    d['title']=title
                    d['url']=url
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
        driver.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
    except:
        break
