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
url = 'https://www.ttecjobs.com/en/careers#'
driver.get(url)

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
   lastCount = lenOfPage
   time.sleep(13)
   lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
   if lastCount==lenOfPage:
        match=True
        Jobs=[]
        Location=driver.find_elements_by_xpath('//div[@class="muted asc-job-public-stats"]')
        Dataset=driver.find_elements_by_xpath('//a[@class="asc-job-left-activate highlight"]')
        for i in range(0,len(Dataset)):
           print(Dataset[i].text)
           print(Dataset[i].get_attribute('data-surl'))
           print(Location[i].text)
           Jobs.append({'title':Dataset[i].text,'url':Dataset[i].get_attribute('data-surl'),'location':Location[i].text})

        print("\n\n")
        print(len(Jobs))
        print("\n\n")
        print(Jobs)
driver.quit()
