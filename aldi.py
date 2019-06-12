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
url = 'https://careers.aldi.us/search-jobs?fl=6252001'
urlsarray=[]
driver.get(url)
for i in range(1,172):
    try:
        driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
        driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
        time.sleep(5)
        links=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
        for link in links:
            title=link.find_element_by_xpath('h2').text
            print(title)
            properlink=link.get_attribute('href')
            print(properlink)
            location=link.find_element_by_xpath('span[@class="job-location"]').text
            print(location)
            d={}
            d['title']=title
            d['location']=location
            d['url']=properlink
            d['comapany']="lilly"
            urlsarray.append(d)
            print(urlsarray)
    except:
        print('this code is working')
        driver.find_element_by_link_text("Next").click()
        time.sleep(15)
        links=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
        for link in links:
            title=link.text
            print(title)
            location=link.find_element_by_xpath('span[@class="job-location"]').text
            properlink=link.get_attribute('href')
            print(properlink)
        #collections.insert_one({'title':title,'joburl':properlink})
print(urlsarray)
print(len(urlsarray))
driver.quit()
