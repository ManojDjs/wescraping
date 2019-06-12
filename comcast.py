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
preferences = {'profile.default_content_setting_values': {'images': 2,
                             'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument('headless')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')

urlsarray=[]
page=1
while page<176:
    try:
       url = 'https://comcast.jibeapply.com/jobs?page='+str(page)
       driver.get(url)
       time.sleep(10)
       page=page+1
       locationlist=[]
       titlelist=[]
       urllist=[]
       element=driver.find_elements_by_xpath('//span[@class="mat-content"]/mat-panel-title/p[@class="job-title"]')
       for i in element:
           title=i.text
           titlelist.append(title)
           print(title)
           url=i.find_element_by_xpath('a').get_attribute('href')
           print(url)
           urllist.append(url)
       locelement=driver.find_elements_by_xpath('//span[@class="mat-content"]/mat-panel-description/div/span/div/p[@class="label-container"]/span/span[@class="ng-star-inserted"]')
       for j in locelement:
           print(j.text)
           location=j.text
           locationlist.append(location)
       if len(titlelist)==len(locationlist):
           for i in range(0,len(titlelist)):
                   d={}
                   d['title']=titlelist[i]
                   d['location']=locationlist[i]
                   d['url']=urllist[i]
                   d['company']="Comcast"
                   urlsarray.append(d)
       print(urlsarray)
       print(len(urlsarray))

    except:pass
