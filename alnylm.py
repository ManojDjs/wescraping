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
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url = 'https://alnylam.taleo.net/careersection/alny_ext/jobsearch.ftl?lang=en'
urlsarray=[]
driver.get(url)
for i in range(1,5):
    time.sleep(5)
    link=driver.find_elements_by_xpath('//div[@class="multiline-data-container"]')
    for l in link:
        title=l.find_element_by_xpath('div/span/a').text
        joburl=l.find_element_by_xpath('div/span/a').get_attribute('href')
        location=l.find_element_by_xpath('div[2]/span').text
        print(title)
        print(joburl)
        print(location)
        d={}
        d['title']=title
        d['location']=location
        d['url']=joburl
        d['comapany']="  Alnylam Pharmaceuticals"
        urlsarray.append(d)
    print(urlsarray)
    print(len(urlsarray))
    time.sleep(3)

    driver.find_element_by_xpath('//a[@id="next"]').click()
driver.quit()
print(len(urlsarray))
print(urlsarray)
