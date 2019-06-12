import time
import re
import threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pymongo
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://admin:jobiak@3.18.238.8:28015/admin")
if(client):
    print("connected")
db = client.stage_jobs
collections = db.project
collections2=db.company
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def amazon3():
        urlsarray=[]
        page=8000
        while page<15000:
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
                        collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'amazon','Recheck':0})
                        d={}
                        d['title']=title
                        d['location']=location
                        d['url']=url
                        d['company']="Amazon"
                        urlsarray.append(d)
                        print(urlsarray)
                        print(len(urlsarray))
               except:break
def compassgroupcareers():
    url='https://jobs.compassgroupcareers.com/search/?searchby=location&createNewAlert=false&q=&locationsearch=&geolocation='
    driver.get(url)
    #driver.find_element_by_xpath('//a[@class="c-button js-filter-careers"]').click()
    time.sleep(3)
    while True:
        for i in range(0,3):
                driver.find_element_by_xpath('//button[@id="tile-more-results"]').click()
                print('page is loading')
                time.sleep(2)
        try:
            link=driver.find_elements_by_xpath('//div[@class="col-md-12 sub-section sub-section-desktop hidden-xs hidden-sm"]/div/div/h2/a')
            for i in link:
                time.sleep(1)
                title=i.text
                url=i.get_attribute('href')
                print(title)
                print(url)
                d={}
                d['title']=title
                d['url']=url
                d['company']='Compass Group careers'
                print(d)
                collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Compass Group careers','Recheck':0})
        except:
            break

def gecareers():
    urlsarray=[]
    page=0
    while True:
        try:
            url='https://jobs.gecareers.com/global/en/search-results?from='+str(page)+'&s=1'
            driver.get(url)
            print(page)
            page=page+10
            time.sleep(10)
            link=driver.find_elements_by_xpath('//li[@class="jobs-list-item"]/div[@class="information"]')
            for i in link:
                url=i.find_element_by_xpath('span/a').get_attribute('href')
                title=i.find_element_by_xpath('span/a').text
                print(url)
                print(title)
                dateposted=i.find_element_by_xpath('p[@class="job-info"]/span/span[@class="job-postdate"]').text
                print(dateposted)
                location=i.find_element_by_xpath('p[@class="job-info"]/span/span[@class="job-location"]').text
                print(location)
                d={}
                d['title']=title
                d['location']=location
                d['url']=url
                d['company']="Ge careers"
                d['datePosted']=dateposted
                collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Ge careers','poastedDate':dateposted,'Recheck':0})
                urlsarray.append(d)
                print(urlsarray)
                print(len(urlsarray))
        except:
            break
def sap():
    urlsarray=[]
    page=0
    while True:
        try:
            url='https://jobs.sap.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
            driver.get(url)
            page=page+25
            time.sleep(3)
            link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in link:
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                title=i.find_element_by_xpath('td/span/a').text
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]').text
                print(title)
                print(url)
                print(location)
                if url not in urlsarray and len(urlsarray)<1100:
                    d={}
                    print(url)
                    d['title']=title
                    d['url']=url
                    d['location']=location
                    d['company']='Sap'
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Sap','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
        except:
            break
def nttdata():
    urlsarray=[]
    page=0
    while True:
        try:
           url = 'https://careers-inc.nttdata.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
           driver.get(url)
           time.sleep(10)
           page=page+25
           element=driver.find_elements_by_xpath('//table/tbody/tr[@class="data-row clickable"]')
           for i in element:
                    title=i.find_element_by_xpath('td[@class="colTitle"]/span/a').text
                    url=i.find_element_by_xpath('td[@class="colTitle"]/span/a').get_attribute('href')
                    print(title)
                    print(url)
                    location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                    print(location)
                    d={}
                    d['title']=title
                    d['location']=location
                    d['url']=url
                    d['company']="NTT DATA, Inc."
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'NTT DATA, Inc.','Recheck':0})
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
        except:break
def advocatehealth():
    urlsarray=[]
    page=0
    while True:
        try:
           url = 'https://jobs.advocatehealth.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=distance&d=10&startrow='+str(page)
           driver.get(url)
           time.sleep(10)
           page=page+25
           element=driver.find_elements_by_xpath('//table/tbody/tr[@class="data-row clickable"]')
           for i in element:
                    title=i.find_element_by_xpath('td/span/a').text
                    url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                    print(title)
                    print(url)
                    location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                    print(location)
                    d={}
                    d['title']=title
                    d['location']=location
                    d['url']=url
                    d['company']="Advocate health careers"
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Kroger','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
        except:break

if __name__ == "__main__":
    # creating thread
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='compassgroupcareers':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                compassgroupcareers()
            elif company=='gecareers':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                gecareers()
            elif company=='advocatehealth':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                advocatehealth()
            elif company=='nttdata':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                nttdata()
            elif company=='sap':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                sap()
            elif company=='amazon3':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon3()
            print('now checked for :'+company)
