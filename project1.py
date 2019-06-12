import time
import re
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
preferences = {'profile.default_content_setting_values': {'images': 2,}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def sheetz():
    page=0
    while True:
        try:
            url='https://jobs.sheetz.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=10&startrow='+str(page)
            driver.get(url)
            page=page+1
            time.sleep(3)
            link=driver.find_elements_by_xpath('//table[@id="searchresults"]/tbody/tr[@class="data-row clickable"]')
            for i in link:
                title=i.find_element_by_xpath('td[@class="colTitle"]/span/a').text
                print(title)
                url=i.find_element_by_xpath('td[@class="colTitle"]/span/a').get_attribute('href')
                print(url)
                location=''
                street=i.find_element_by_xpath('td[@class="colDepartment hidden-phone"]/span').text
                area=i.find_element_by_xpath('td[@class="colLocation hidden-phone"]/span').text
                location=street+'  '+area
                print(location)
                jobTYpe=i.find_element_by_xpath('td[@class="colShifttype hidden-phone"]/span').text
                print(jobTYpe)
                collections.insert_one({'url':url,'title':title,stat:'','location':location,'jobType':jobTYpe,'company':'sheetz','Recheck':0})
        except:
            break
def sanofi():
    url='https://en.jobs.sanofi.com/search-jobs'
    urlsarray=[]
    count=1
    driver.get(url)
    while True:
        try:
            driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
            textarea=driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(count)
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
                    collections.insert_one({'url':joblink,'title':jobtitle,'location':makeitastring,'jobType':'','company':'Sanofi','Recheck':0})
            count=count+1
            print(urlsarray)
            print(len(urlsarray))
        except:break
def amazon():
        urlsarray=[]
        page=20000
        while page<30000:
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
def jpmorgan():
    driver.set_page_load_timeout(300)
    while True:
            r=1
            URL="https://jobs.jpmorganchase.com/ListJobs/All/Page-"+str(r)
            print(URL)
            driver.get(URL)
            urlsarray=[]
            time.sleep(3)
            try:
                jobTitle = driver.find_elements_by_xpath('//section[@id="job-list"]/div/div[2]/table/tbody/tr/td[2]/a')
                location = driver.find_elements_by_xpath('//td[@class="colcity"]')
                loc1 = driver.find_elements_by_xpath('//td[@class="colstate"]')
                loc2 = driver.find_elements_by_xpath('//td[@class="colcountry"]')
                jobUrl = driver.find_elements_by_xpath('//section[@id="job-list"]/div/div[2]/table/tbody/tr/td[2]/a')
                jobId = driver.find_elements_by_xpath('//td[@class="coldisplayjobid"]')
                num_page_items = len(jobUrl)
                r=r+1
                for i in range(num_page_items):
                    print(jobTitle[i].text + " : " + location[i].text +","+loc1[i].text +":" + jobUrl[i].get_attribute('href') + ":" + jobId[i].text)
                    data = {'Label':jobTitle[i].text ,'title':jobTitle[i].text, 'Link':jobUrl[i].get_attribute('href'), 'location':location[i].text+","+loc1[i].text+","+loc2[i].text,
                            'jobId':jobId[i].text, 'company':'JP morgan','Recheck':0}
                    collections.insert_one(data)
                    urlsarray.append(data)
                    print(urlsarray)
                    print(len(urlsarray))
                print(urlsarray)
            except:break
def lululemon():
    url = 'https://info.lululemon.com/careers/store-jobs'
    urlsarray=[]
    driver.get(url)
    try:
        for i in range(1,140):
            driver.find_element_by_xpath('//div[@class="more-button"]/a[@class="button load-more-jobs"]').click()
        time.sleep(15)
        e=driver.find_elements_by_xpath('//table/tbody/tr[@class="clickable-row"]')
        for i in e:
            title=i.find_element_by_xpath('td/a').text
            print(title)
            url=i.find_element_by_xpath('td/a').get_attribute('href')
            print(url)
            collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'lululemon','Recheck':0})
            d={}
            d['url']=url
            d['title']=title
            d['comapany']='lululemon'
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
    except:
        time.sleep(25)
        e=driver.find_elements_by_xpath('//table/tbody/tr[@class="clickable-row"]')
        for i in e:
            title=i.find_element_by_xpath('td/a').text
            print(title)
            url=i.find_element_by_xpath('td/a').get_attribute('href')
            print(url)
            collections.insert_one({'url':url,'title':title,'location':'','jobType':'','company':'lululemon','Recheck':0})
            d={}
            d['url']=url
            d['title']=title
            d['comapany']='lululemon'
            urlsarray.append(d)
            print(urlsarray)
            print(len(urlsarray))
        pass
        #collections.insert_one({'title':title,'joburl':properlink})
    print(urlsarray)
    print(len(urlsarray))
if __name__ == "__main__":
    # creating thread
    checker=collections2.find({'Recheck':0})
    for check in checker:
            company=check['company']
            if company=='amazon':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                amazon()
            elif company=='jpmorgan':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                jpmorgan()
            elif company=='lululemon':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                lululemon()
            elif company=='sanofi':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                sanofi()
            elif company=='sheetz':
                collections2.update_one({'company':company},{'$set':{'Recheck':1}})
                sheetz()
            print(company+'not found in this program')
