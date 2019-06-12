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
url = 'https://www.att.jobs/search-jobs'
urlsarray=[]
driver.get(url)
for i in range(0,121):
    try:
        driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
        time.sleep(5)
        locationlist=[]
        titlelist=[]
        urllist=[]
        print(i)
        e= driver.find_elements_by_xpath('//div[@id="search-results-list"]/ul/li/a')
        for i in e:
            title=i.find_element_by_xpath('h2').text
            print(title)
            url=i.get_attribute('href')
            print(url)
            location=i.find_element_by_xpath('span[@class="job-location-search"]').text
            print(location)
            d={}
            d['title']=title
            d['location']=location
            d['url']=url
            d['comapany']="AT&T"
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
    except:pass
print(urlsarray)
print(len(urlsarray))
driver.quit()
