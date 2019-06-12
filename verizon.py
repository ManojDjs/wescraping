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
preferences = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
#options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')

urlsarray=[]
page=1
while True:
    try:
       url = 'https://www.verizon.com/about/work/search/jobs?location=&location_country=&location_state=&ns_dist=50&page='+str(page)+'&per_page=&q=&radius=&sort_by=&v_location=&v_m=false'
       driver.get(url)
       time.sleep(2)
       page=page+1
       e=driver.find_elements_by_xpath('//td[@class="jobs_table_item_title"]/a')
       for i in e:
           print(i.get_attribute('href'))
           title=i.text
           url=i.get_attribute('href')
           d={}
           d['url']=i.get_attribute('href')
           d['title']=title
           d['company']='Verizon'
           print(urlsarray)
           urlsarray.append(d)
           print(len(urlsarray))
    except:pass
