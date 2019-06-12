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
preferences = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
#options.add_argument('user-data-dir=./chromeprofile');
#options.add_argument('disable-infobars');
options.add_argument("disable-notifications");
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url = 'https://job-search.astrazeneca.com/search-jobs'
urlsarray=[]
driver.get(url)
for i in range(1,127):
    driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
    driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
    driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
    #driver.find_element_by_xpath('//input[@class="pagination-current"]').submit()
    time.sleep(10)
    link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
    for l in link:
        title=l.find_element_by_xpath('h2').text
        print(title)
        joburl=l.get_attribute('href')
        print(joburl)
        location=l.find_element_by_xpath('//div[@class="job-location job-info"]').text
        print(location)
        print("""""""""""""""""""""""""""""""")
        d={}
        d['title']=title
        d['location']=location
        d['url']=joburl
        d['comapany']="AstraZeneca"
        urlsarray.append(d)
        print(urlsarray)
    time.sleep(2)
driver.quit()
print(urlsarray)
print(len(urlsarray))
