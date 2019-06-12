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
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
urlsarray=[]
page=1
while True:
    try:
        url='https://www.usajobs.gov/Search/Results?d=VA&p='+str(page)
        driver.get(url)
        page=page+1
        time.sleep(3)
        link=driver.find_elements_by_xpath('//div[@id="usajobs-search-results"]/div[@class="usajobs-search-result--core"]')
        for i in link:
            title=i.find_element_by_xpath('a').text
            url=i.find_element_by_xpath('a').get_attribute('href')
            print(title)
            print(url)
            location=i.find_element_by_xpath('div/div/h4[@class="usajobs-search-result--core__location"]/span').text
            print(location)
            if url not in urlsarray:
                d={}
                print(url)
                d['title']=title
                d['url']=url
                d['location']=location
                d['company']='USA Jobs'
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
    except:
        break
