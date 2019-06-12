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
page=10
while page<120:
       url = 'https://www.amazon.jobs/en/search?offset='+str(page)+'&result_limit=10&sort=relevant&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&'
       driver.get(url)
       time.sleep(3)
       page=page+10
       element=driver.find_elements_by_xpath('//div[@class="job-tile-lists col-12"]/div[@class="job-tile"]')
       for i in element:
            url=i.find_element_by_xpath('a').get_attribute('href')
            print(url)
            title=i.find_element_by_xpath('a/div[@class="job"]/div/div/h3[@class="job-title"]').text
            print(title)
            location=i.find_element_by_xpath('a/div[@class="job"]/div/div/p[@class="location-and-id"]').text
            print(location)
            d={}
            d['title']=title
            d['location']=location
            d['url']=url
            d['company']="Amazon"
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
driver.quit
print(urlsarray)
