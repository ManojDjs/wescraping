import time
import re
from selenium import webdriver
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/baiscs")
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
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url = 'https://en.jobs.sanofi.com/search-jobs'
urlsarray=[]
driver.get(url)
for i in range(1,226):
    driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
    textarea=driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
    button=driver.find_element_by_xpath("//button[@class='pagination-page-jump']").click()
    time.sleep(5)
    links=driver.find_elements_by_xpath('//div[@id="search-results-list"]/ul/li/a')
    for link in links:
        title=link.text
        titleandloc =title.split("\n")
        jobtitle=titleandloc[0]
        jonloc=titleandloc[1].split(" ")
        k=len(jonloc)-1
        makeitastring = ' '.join(map(str, jonloc[0:k]))
        print(jobtitle)
        print(makeitastring)
        joblink=link.get_attribute('href')
        print(joblink)
        if link not in urlsarray:
            d={}
            d['title']=jobtitle
            d['location']=makeitastring
            d['url']=joblink
            d['comapany']="Sanofi"
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
print(urlsarray)
driver.quit()
print(len(urlsarray))
