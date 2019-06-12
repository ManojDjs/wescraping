import time
from selenium import webdriver
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/baiscs")
if(client):
    print("connected")
db = client.Appcast
collections = db.careerjobs
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
doc=collections.find({})
urlsarray=[]
for i in doc:
    driver.get(i['joburl'])
    d={}
    jobtitle=i['title']
    try:
       location=driver.find_element_by_xpath('//span[@class="jobGeoLocation"]').text
    except:
        location="NULL"
    d['title']=jobtitle
    d['location']=location
    d['url']=i['joburl']
    d['comapany']="TE jobs"
    print(d)
    urlsarray.append(d)


driver.quit()
print(urlsarray)
print(len(urlsarray))
