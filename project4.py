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
def amazon4():
        urlsarray=[]
        page=12000
        while True:
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
def walmart():
    urlsarray=[]
    page=1
    while True:
        try:
            url = 'https://careers.walmart.com/results?q=&page='+str(page)+'&sort=rank&expand=department,brand,type,rate&jobCareerArea=all'
            driver.get(url)
            time.sleep(3)
            page=page+1
            loc=driver.find_elements_by_xpath('//div[@class="search__results"]/ul/li[@class="search-result job-listing   "]')
            for i in loc:
                title=i.find_element_by_xpath('div/h4/a').text
                url=i.find_element_by_xpath('div/h4/a').get_attribute('href')
                location=i.find_element_by_xpath('div[@class="job-listing__info"]/span[@class="job-listing__location"]').text
                print(title)
                print(url)
                print(location)
                d={}
                d['title']=title
                d['url']=url
                d['company']='walmart'
                collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'walmart','Recheck':0})
            print(urlsarray)
        except:break
def verizon():
    urlsarray=[]
    page=1
    while True:
        try:
           url = 'https://www.verizon.com/about/work/search/jobs?location=&location_country=&location_state=&ns_dist=50&page='+str(page)+'&per_page=&q=&radius=&sort_by=&v_location=&v_m=false'
           driver.get(url)
           time.sleep(2)
           page=page+1
           e=driver.find_elements_by_xpath('//td[@class="jobs_table_item_title"]/a')
           for i in e:
               print(i.get_attribute('href'))
               title=i.text
               url=i.get_attribute('href')
               d={}
               d['url']=i.get_attribute('href')
               d['title']=title
               d['company']='Verizon'
               print(urlsarray)
               urlsarray.append(d)
               collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Verizon','Recheck':0})
               print(len(urlsarray))
        except:break
def intel():
    urlsarray=[]
    page=1
    while True:
        try:
            url = 'https://jobs.intel.com/ListJobs/All/Page-'+str(page)
            driver.get(url)
            time.sleep(5)
            page=page+1
            loc=driver.find_elements_by_xpath('//td[@class="coljobtitle"]/a')
            for i in loc:
                title=i.text
                url=i.get_attribute('href')
                print(title)
                print(url)
                d={}
                d['title']=title
                d['url']=url
                d['company']='Intel'
                print(d)
                collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Intel','Recheck':0})
                urlsarray.append(d)
            print(urlsarray)
        except:break
def dsw():
    urlsarray=[]
    page=0
    while True:
        try:
            url = 'https://careers.dswinc.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=10&startrow='
            driver.get(url)
            time.sleep(3)
            page=page+25
            loc=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in loc:
                title=i.find_element_by_xpath('td/span/a').text
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                print(title)
                print(url)
                print(location)
                d={}
                d['title']=title
                d['url']=url
                d['company']='DSW'
                print(d)
                collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'DSW','Recheck':0})
                urlsarray.append(d)
            print(urlsarray)
        except:break
def kwiktrip():
    urlsarray=[]
    page=0
    while True:
        try:
            url = 'https://jobs.kwiktrip.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=distance&d=10&startrow='+str(page)
            driver.get(url)
            time.sleep(3)
            page=page+25
            loc=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in loc:
                title=i.find_element_by_xpath('td/span/a').text
                url=i.find_element_by_xpath('td/span/a').get_attribute('href')
                location=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                print(title)
                print(url)
                print(location)
                d={}
                d['title']=title
                d['url']=url
                d['company']='Kwik Trip'
                print(d)
                collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Kwik Trip','Recheck':0})
                urlsarray.append(d)
            print(urlsarray)
        except:break
if __name__ == "__main__":
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='walmart':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                walmart()
            elif company=='verizon':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                verizon()
            elif company=='intel':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                intel()
            elif company=='dsw':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                dsw()
            elif company=='kwiktrip':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                kwiktrip()
            elif company=='amazon4':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon4()
            print('now checked for :'+company)

