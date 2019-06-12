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
preferences = {'profile.default_content_setting_values': { 'images': 2}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
url = 'https://en.jobs.sanofi.com/job/shanghai/database-project-expert-pv-sh/20873/11924537'
urlsarray=[]
driver.get(url)
time.sleep(5)
listelements=[]
joblocation=''
address1=''
adress2=''
jobId=''
jobType=''
location=driver.find_element_by_xpath('//div[@class="clearfix job-vital-info"]').text
location=str(location).split('\n')
for i in location:
        listelements.append(i)
index=1
for j in listelements:
    if 'JOB ID' in j:
        jobId=listelements[index]
        print(listelements[index])
    if 'DATE POSTED' in j:
        dateposted=listelements[index]
        print('datePosted'+listelements[index])
    if 'LOCATION' in j:
        adress2=listelements[index]
    if  'CONTRACT TYPE' in j:
        print('JobType '+listelements[index])
        jobType=listelements[index]
    index=index+1
joblocation=adress2
print('JOB LOCATION IS '+ joblocation)
jobdescription=driver.find_element_by_xpath('//div[@class="ats-description"]').get_attribute('innerHTML')
print(jobdescription)

