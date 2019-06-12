import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.sanofi
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2,
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
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument('user-data-dir=./chromeprofile');
#options.add_argument('disable-infobars');
options.add_argument("disable-notifications");
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
page=0
urlsarray=[]
while True:
    try:
        url='https://globalcareers-waters.icims.com/jobs/search?pr='+str(page)+'&schemaId=&o='
        driver.get(url)
        time.sleep(15)
        print(page)
        print('is clicked')
        page=page+1
        element=driver.find_elements_by_xpath('//div[@class="row"]')
        print(element)
        for i in element:
            print(i.text)
        '''d={}
        d['title']=title
        d['location']=location
        d['url']=url
        d['company']=""
        urlsarray.append(d)
        print(urlsarray)
        print(len(urlsarray))'''
    except:
        print('no data clicked')
        pass
driver.quit()
