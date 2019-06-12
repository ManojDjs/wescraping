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
while True:
    try:
       url = 'https://jobs.advocatehealth.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=distance&d=10&startrow='+str(page)
       driver.get(url)
       time.sleep(10)
       page=page+25
       element=driver.find_elements_by_xpath('//table/tbody/tr[@class="data-row clickable"]')
       for i in element:
                title=i.find_element_by_xpath('td/span/a').text
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                print(title)
                print(url)
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                print(location)
                d={}
                d['title']=title
                d['location']=location
                d['url']=url
                d['company']="Kroger"
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
    except:break
