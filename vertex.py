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
#options.add_argument('user-data-dir=./chromeprofile');
#options.add_argument('disable-infobars');
options.add_argument("disable-notifications");
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
page=0
url='https://recruiting.paylocity.com/recruiting/jobs/List/2428/LakePharma-Inc'
driver.get(url)
time.sleep(10)
element=driver.find_elements_by_xpath('//div[@class="job-listing-container"]/div[@class="row"]')
for i in element:
    print(i.find_element_by_xpath('span/div[@class="row job-listing-job-item"]/div/span[@class="job-item-title"]/a').text)
    url=i.find_element_by_xpath('span/div[@class="row job-listing-job-item"]/div/span[@class="job-item-title"]/a').get_attribute('href')
    print

urlsarray=[]


#driver.quit()
