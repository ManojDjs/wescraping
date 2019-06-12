import time
from selenium import webdriver
import pymongo
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
url = 'https://www.takedajobs.com/search-jobs?glat=3.15806007385254&glon=101.712997436523'
urlsarray=[]
driver.get(url)
for i in range(1,95):
    driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
    textarea=driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
    driver.find_element_by_xpath('//div[@class="pagination-paging"]/a[@class="next"]').click()
    time.sleep(10)
    links=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
    for link in links:
        titlelist=[]
        titlelist=link.text.split('\n')
        title=titlelist[0]
        location=titlelist[1]
        print(title)
        print(location)
        properlink=link.get_attribute('href')
        print(properlink)
        d={}
        d['title']=title
        d['location']=location
        d['url']=properlink
        d['comapny']="Takeda"
        urlsarray.append(d)
        print(urlsarray)
        print(len(urlsarray))
driver.quit()
print(len(urlsarray))
