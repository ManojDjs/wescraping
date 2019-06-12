import time
import re
import threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
if(client):
    print("connected")
db = client.stage_jobs
collections = db.project
collections2=db.company
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': {'images': 2,}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def usajobs():
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
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'USA Jobs','Recheck':0})
        except:
            break
def microsoft():
    urlsarray=[]
    page=0
    while page<4500:
           url = 'https://careers.microsoft.com/us/en/search-results?from='+str(page)+'&s=1&rt=professional'
           driver.get(url)
           time.sleep(10)
           page=page+20
           element=driver.find_elements_by_xpath('//div[@class="information"]')
           for i in element:
                    title=i.find_element_by_xpath('a/span[@class="job-title"]').text
                    url=i.find_element_by_xpath('a').get_attribute('href')
                    print(title)
                    print(url)
                    d={}
                    d['title']=title
                    d['url']=url
                    d['company']="Microsoft"
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
                    collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Microsoft','Recheck':0})

def amazon1():
        urlsarray=[]
        page=10
        while page<4000:
               url = 'https://www.amazon.jobs/en/search?offset='+str(page)+'&result_limit=10&sort=relevant&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&'
               driver.get(url)
               time.sleep(4)
               page=page+10
               try:
                   element=driver.find_elements_by_xpath('//div[@class="job-tile-lists col-12"]/div[@class="job-tile"]')
                   for i in element:
                        url=i.find_element_by_xpath('a').get_attribute('href')
                        print(url)
                        title=i.find_element_by_xpath('a/div[@class="job"]/div/div/h3[@class="job-title"]').text
                        print(title)
                        location=i.find_element_by_xpath('a/div[@class="job"]/div/div/p[@class="location-and-id"]').text
                        print(location)
                        d={}
                        d['title']=title
                        d['location']=location
                        d['url']=url
                        d['company']="Amazon"
                        urlsarray.append(d)
                        collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'amazon','Recheck':0})

                        print(urlsarray)
                        print(len(urlsarray))
               except:break
def capgemini():
    urlsarray=[]
    page=0
    while True:
        try:
            url='https://jobs.capgemini.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
            driver.get(url)
            page=page+25
            time.sleep(3)
            link=driver.find_elements_by_xpath('//tr[@class="data-row clickable"]')
            for i in link:
                title=i.find_element_by_xpath('td/span/a').text
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                print(title)
                print(url)
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                print(location)
                if url not in urlsarray:
                    d={}
                    print(url)
                    d['title']=title
                    d['url']=url
                    d['location']=location
                    d['company']='Capgemini'
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Capgemini','Recheck':0})

                    print(urlsarray)
                    print(len(urlsarray))
        except:
            break

def texasroad():
    urlsarray=[]
    url='https://careers.texasroadhouse.com/ListJobs'
    driver.get(url)
    while True:
        try:
            time.sleep(5)
            link=driver.find_elements_by_xpath('//tbody[@role="rowgroup"]/tr')
            for i in link:
                title=i.find_element_by_xpath('td/a').text
                print(title)
                url=i.find_element_by_xpath('td/a').get_attribute('href')
                print(url)
                address1=i.find_element_by_xpath('td[@class="ShortTextField3-cell"]').text
                address2=i.find_element_by_xpath('td[@class="ShortTextField4-cell"]').text
                location=address1+' '+address2
                print(location)
                if url not in urlsarray :
                    d={}
                    print(url)
                    d['title']=title
                    d['url']=url
                    d['location']=location
                    d['company']='Texas Roadhouse'
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Texas Roadhouse','Recheck':0})
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
            try:
              driver.find_element_by_xpath("//span[contains(text(), 'arrow-e')]").click()
            except:
                driver.find_element_by_xpath('//a[@class="k-link k-pager-nav"]/span').click()
        except:break
def unitedtechnology():
    url = 'https://jobs.utc.com/search-jobs/united%20states?orgIds=1566-23744&kt=1'
    urlsarray=[]
    driver.get(url)
    p=1
    while True:
        try:
            driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
            driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(p)
            driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
            time.sleep(5)
            link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
            for i in link:
                    url=i.get_attribute('href')
                    title=i.text
                    print(title)
                    print(url)
                    d={}
                    d['title']=title
                    d['url']=url
                    d['company']="United technologies"
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
                    collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'United technologies','Recheck':0})
            p=p+1
        except:break

if __name__ == "__main__":
    # creating thread
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='amazon6':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon1()
            elif company=='microsoft':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                microsoft()
            elif company=='usajobs':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                usajobs()
            elif company=='capgemini':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                capgemini()
            elif company=='texasroad':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                texasroad()
            elif company=='unitedtechnology':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                unitedtechnology()
            print(company+'not found in this program')
