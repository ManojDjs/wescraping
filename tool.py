import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
#options.add_argument('user-data-dir=./chromeprofile');
#options.add_argument('disable-infobars');
options.add_argument("disable-notifications");
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
def type1():
    page=0
    while True:
        try:
           url='https://www.merckgroup.com/en/careers/job-search.html?query%3A%2Cpage%3A'+str(page)+'%2Ccountry%3Aall%2Cstate%3Aall%2Ccity%3Aall%2CfunctionalArea%3Aall%2CcareerLevel%3Aall%2CemploymentType%3Aall'
           driver.get(url)
           time.sleep(8)
           print(page)
           print('is clicked')
           page=page+1
        except:
            print('no data clicked')
            break
            pass
    driver.quit()
def type2(url):
    try:
        driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
        #url = 'https://jobs.sanofi.us/search-jobs/Boston%2C%20MA/507-18104/4/6252001-6254926-4952349-4930956/42x3584/-71x0598/50/2'
        urlsarray=[]
        driver.get(url)
        for i in range(1,15):
            driver.find_element_by_xpath('//input[@class="pagination-current"]').clear()
            textarea=driver.find_element_by_xpath('//input[@class="pagination-current"]').send_keys(i)
            button=driver.find_element_by_xpath("//button[@class='pagination-page-jump']").click()
            time.sleep(5)
            links=driver.find_elements_by_xpath('//section[@id="search-results-list"]/ul/li/a')
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
        driver.quit()
        print(len(urlsarray))
    except:return None
url=input('enter url')
if 'merkgroup' in  url:
    type1()
else:
    type2(url)
