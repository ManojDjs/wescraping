import time
import re
from selenium.webdriver.common.keys import Keys
import threading
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
preferences = {'profile.default_content_setting_values': { 'images': 2,
                            }}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def amazon2():
        urlsarray=[]
        page=4000
        while page<8000:
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
def marriott():
    r=1
    while True:
        try:
            URL="https://jobs.marriott.com/marriott/jobs?page="+str(r)+"&limit=100"
            print(URL)
            driver.get(URL)
            time.sleep(10)
            jobTitle = driver.find_elements_by_xpath('//mat-panel-title/p/a/span')
            Location = driver.find_elements_by_xpath('//mat-panel-description/div/span/div/p/span[@itemprop="jobLocation"]')
            jobUrl = driver.find_elements_by_xpath('//mat-panel-title/p/a')
            jobId = driver.find_elements_by_xpath('//mat-panel-title/p[2]/span')
            num_page_items = len(jobUrl)
            r=r+1
            for i in range(num_page_items):
              print(jobTitle[i].text + " : " + Location[i].text + ":" + jobUrl[i].get_attribute('href') + ":" + jobId[i].text)
              data = {'Label':jobTitle[i].text , 'Link':jobUrl[i].get_attribute('href'), 'location':Location[i].text,
                  'jobId':jobId[i].text,'Recheck':0, 'company':'Marriott Careers'}
              collections.insert_one(data)
            time.sleep(2)
        except:break
def kroger():
    urlsarray=[]
    page=0
    while True:
        try:
           url = 'https://jobs.kroger.com/search/?q=&sortColumn=referencedate&sortDirection=desc&startrow='+str(page)
           driver.get(url)
           time.sleep(10)
           page=page+10
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
                    d['company']="Kroger"
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Kroger','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
        except:break
def capitalonecareers():
    url = 'https://www.capitalonecareers.com/search-jobs'
    urlsarray=[]
    driver.get(url)
    i=1
    while True:
        try:
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
                    location=i.find_element_by_xpath('span').text
                    print(location)
                    d={}
                    d['title']=title
                    d['location']=location
                    d['url']=url
                    d['company']="Capitalone careers"
                    urlsarray.append(d)
                    collections.insert_one({'url':url,'title':title,'location':location,'jobType':'','company':'Capitalone careers','Recheck':0})
                    print(urlsarray)
                    print(len(urlsarray))
            i=i+1
            print(urlsarray)
            print(len(urlsarray))
        except:break

def medtronic():
    url = 'https://jobs.medtronic.com/jobs/search/77457747'
    jobs=1
    urlsarray=[]
    while True:
        try:
            driver.get(url+"page"+str(jobs))
            time.sleep(8)
            urlsofjob=driver.find_elements_by_xpath('//div[@class="jlr_title"]')
            for link in urlsofjob:
                jobtitle=link.find_element_by_xpath('p/a').text
                print("jobtitle:" + jobtitle)
                propoerlink=link.find_element_by_xpath('p/a').get_attribute('href')
                print(propoerlink)
                location=link.find_element_by_xpath('p/span[@class="location"]').text
                print(location)
                d={}
                d['title']=jobtitle
                d['location']=location
                d['url']=propoerlink
                d['company']="Medtronic"
                urlsarray.append(d)
                collections.insert_one({'url':propoerlink,'title':jobtitle,'location':location,'jobType':'','company':'Medtronic','Recheck':0})
                print(urlsarray)
                print(len(urlsarray))
            jobs=jobs+1
        except:break
def bankofamerica():
    urlsarray=[]
    url='https://careers.bankofamerica.com/search-jobs.aspx?c=united-states&r=us'
    driver.get(url)
    while True:
        try:
            time.sleep(35)
            link=driver.find_elements_by_xpath('//td[@class="jobtitle"]/a')
            for i in link:
                time.sleep(1)
                url=i.get_attribute('href')
                title=i.text
                print(title)
                if url not in urlsarray:
                    print(url)
                    d={}
                    if url in urlsarray:
                        print('already innnn')
                    else:
                        d['title']=title
                        d['url']=url
                        urlsarray.append(d)
                        print(urlsarray)
                        print(len(urlsarray))
                        collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'Bank of america','Recheck':0})
            driver.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
        except:
            break
if __name__ == "__main__":
    # creating thread
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='kroger':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                kroger()
            elif company=='marriott':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                marriott()
            elif company=='bankofamerica':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                bankofamerica()
            elif company=='medtronic':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                medtronic()
            elif company=='capitalonecareers':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                capitalonecareers()
            elif company=='amazon4':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon2()
            print('now checked for :'+company)
