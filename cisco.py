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
preferences = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')

urlsarray=[]
page=0
while page<1440:
    try:
       url = 'https://jobs.cisco.com/jobs/SearchJobs/?3_109_3=%5B"169482"%5D&projectSort=schemaField_3_84_3&projectSortDirection=DESC&&projectOffset='+str(page)
       driver.get(url)
       time.sleep(10)
       page=page+25
       locationlist=[]
       titlelist=[]
       urllist=[]
       element=driver.find_elements_by_xpath('//tbody/tr/td[@data-th="Job Title"]')
       for i in element:
                title=i.text
                print(title)
                titlelist.append(title)
                url=i.find_element_by_xpath('a').get_attribute('href')
                print(url)
                urllist.append(url)
       locationelement=driver.find_elements_by_xpath('//tbody/tr/td[@data-th="Location"]')
       for j in locationelement:
           print(j.text)
           location=j.text
           locationlist.append(location)
       if len(titlelist)==len(locationlist):
           for i in range(0,len(titlelist)):
                   d={}
                   d['title']=titlelist[i]
                   d['location']=locationlist[i]
                   d['url']=urllist[i]
                   d['company']="Cisco"
                   urlsarray.append(d)
       print(urlsarray)
       print(len(urlsarray))
    except:pass
