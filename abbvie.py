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

for i in range(1,70):
       url = 'https://abbvie.referrals.selectminds.com/jobs/search/3773090/page'+str(i)
       driver.get(url)
       time.sleep(2)
       element=driver.find_elements_by_xpath('//div[@class="jlr_title"]')
       for i in element:
           jobtitle=i.find_element_by_xpath('p/a[@class="job_link font_bold"]').text
           print(jobtitle)
           joburl=i.find_element_by_xpath('p/a[@class="job_link font_bold"]').get_attribute('href')
           print(joburl)
           joblocation=i.find_element_by_xpath('p[2]/span[2]').text
           print(joblocation)
           d={}
           d['title']=jobtitle
           d['location']=joblocation
           d['url']=joburl
           d['comapany']="abbive"
           urlsarray.append(d)
print(urlsarray)
print(len(urlsarray))
