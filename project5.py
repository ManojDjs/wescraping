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
preferences = {'profile.default_content_setting_values': {'images': 2,}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def checkersdrive():
    urlsarray=[]
    page=0
    while True:
        try:
            url='https://careers.checkers.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
            driver.get(url)
            page=page+25
            time.sleep(5)
            link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in link:
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                title=i.find_element_by_xpath('td/span/a').text
                print(title)
                print(url)
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                postedDate=i.find_element_by_xpath('td[@class="colDate hidden-phone"]/span').text
                if url not in urlsarray:
                    d={}
                    print(url)
                    d['title']=title
                    d['url']=url
                    d['location']=location
                    d['company']='Checkers Drive-In Restaurants'
                    d['postedDate']=postedDate
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','postaedDate':postedDate,'company':'Checkers Drive-In Restaurants','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
        except:
            break
def luxottica():
    urlsarray=[]
    page=0
    while True:
        try:
            url='https://jobs.luxottica.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
            driver.get(url)
            page=page+30
            time.sleep(3)
            link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in link:
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                title=i.find_element_by_xpath('td/span/a').text
                print(title)
                print(url)
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                if url not in urlsarray and len(urlsarray)<1100:
                    d={}
                    print(url)
                    d['title']=title
                    d['url']=url
                    d['location']=location
                    d['company']='Luxottica Group S.p.A.'
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','postaedDate':'','company':'Luxottica Group S.p.A.','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
        except:
            break
def amazon5():
        urlsarray=[]
        page=20000
        while page<25000:
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
def allieduniversal():
    url = 'https://jobs.aus.com/search-jobs?fl=6252001,4566966,6251999'
    urlsarray=[]
    driver.get(url)
    try:
        for i in range(1,147):
            driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
            driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
            driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(Keys.ENTER)
            time.sleep(5)
            link=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
            for i in link:
                    url=i.get_attribute('href')
                    title=i.find_element_by_xpath('h2').text
                    print(title)
                    print(url)
                    location=i.find_element_by_xpath('span[@class="job-location"]').text
                    print(location)
                    jobid=i.find_element_by_xpath('span[@class="job-id"]').text
                    d={}
                    d['title']=title
                    d['location']=location
                    d['url']=url
                    d['company']='Allied Universal'
                    d['jobId']=jobid
                    urlsarray.append(d)
                    print(urlsarray)
                    print(len(urlsarray))
                    collections.insert_one({'url':url,'title':title,'location':location,'jobId':jobid,'company':'Allied Universal','Recheck':0})
    except:pass
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
                    collections.insert_one({'url':url,'title':title,'location':'','jobId':'','company':'United technologies','Recheck':0})
            p=p+1
        except:break

if __name__ == "__main__":
    # creating thread
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='amazon5':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon5()
            elif company=='allieduniversal':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                allieduniversal()
            elif company=='luxottica':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                luxottica()
            elif company=='checkersdrive':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                checkersdrive()
            elif company=='unitedtechnology':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                unitedtechnology()
            print('now checked for :'+company)
