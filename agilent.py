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
                             'auto_select_certificate': 2, 'fullscreen': 2,
                             'mixed_script': 2, 'media_stream': 2,
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
url = 'https://recruiting.adp.com/srccar/public/RTI.home?c=2167807&d=External&_ga=2.187917866.344956060.1556088425-1239995808.1556088425'
urlsarray=[]
driver.get(url)
for i in range(1,63):
    driver.find_element_by_xpath('//div[@class="page"]/input[@id="page_"]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//div[@class="page"]/input[@id="page_"]').send_keys(i)
    driver.find_element_by_xpath('//div[@class="page"]/input[@id="page_"]').send_keys(Keys.ENTER)
    time.sleep(10)

