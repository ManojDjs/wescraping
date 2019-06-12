import time
from bigml.api import BigML
from bigml.deepnet import Deepnet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import PyPDF2 
import statistics
import requests
from pymongo import MongoClient
import xlrd
import os.path
import json
import csv
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import Comment
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


BIGML_USERNAME = 'jobiakmldev'
BIGML_API_KEY = 'd0ad30e1fa62ba453db353e2e6680866c0393cfb'
BIGML_STORAGE = 'D://Empty'
api = BigML(BIGML_USERNAME, BIGML_API_KEY, storage=BIGML_STORAGE)
deepnet = Deepnet('deepnet/5b867d8c8bf7d57a4302f787', api=api)


con = MongoClient('localhost', 27017)
db = con['Url_data']
collection=db['getJobs']

add_all_jobs=[]
flag=0
list_=[]
rep_val=''
store_first_keyword=''


def insert_text_in_textBox():
    try:
        if(len(browser.find_elements_by_xpath("//input[@type='text']"))>=1):
            text_box = browser.find_elements_by_xpath("//input[@type='text']")
            text_box[0].send_keys("jobs")
    except:
        pass    


def get_all_jobs(url,original_url,valid_urls):
    valid_urls=valid_urls[valid_urls.index(url):]
    print(len(valid_urls))
    print()
    browser.get(original_url)
    try:
        ele=find_elements_by_class_name('pagination')
        
    except:
        pass
    return valid_urls

def iterateAnchors(get_links):
    for i in get_links:
        browser.get(i)
        time.sleep(1)
        get_all_valid_links()

def get_all_valid_links():
    print('In get_all_valid_links')
    alllinks = []
    innerHTML=browser.execute_script('return document.body.innerHTML')
    iframes = browser.find_elements_by_tag_name('iframe')
    no_of_iframes = len(iframes)
    if(no_of_iframes > 0):
        for i in range(0, len(iframes)):
            try:
                f = browser.find_elements_by_tag_name('iframe')[i]
                browser.switch_to.frame(i)
                innerHTML=browser.execute_script('return document.body.innerHTML')
                elems = browser.find_elements_by_xpath("//a[@href]")
                for uma in elems:
                    try:
                        if (uma.text != ''):
                            store_both = {"url": uma.get_attribute('href'), "label": uma.text.replace("\n", " ") + "+-"}
                            alllinks.append(store_both)
                    except:
                        pass
                browser.switch_to_default_content()
            except:
                pass
    links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', innerHTML)
    for link in links:
        try:
            linktext = str(link).replace("&quot;);", "")
            linktext = linktext.rstrip('/')
            linktext = linktext.split('/')[-1]
            linktext = linktext.replace('-',' ').replace('\n',' ').title()
            link_label_json = {'url': link, 'label': linktext}
            alllinks.append(link_label_json)
        except:
            pass
    elems = browser.find_elements_by_xpath("//a[@href]")
    get_anchors=[]
    add=[]
    get_links=[]
    for uma in elems:
        try:
            if(uma.text!=''):
                store_both = {"url": uma.get_attribute('href'), "label": uma.text.replace("\n"," ")+"+-"}
                alllinks.append(store_both)
        except:
            pass
    
    add=json.dumps(alllinks)
    data = {
        'labelitems': add
        }
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    try:
        response = requests.post('http://ijiraq.dev.bigml.com/identify/label/jobtitle',  data=data,headers=headers).json()
        print("Got anchor links of a page")
        remove_dupli=[]
        for i in response:
            if((i['confidence']*100)>60):
                remove_dupli.append(i['url'])
        remove_dupli=set(remove_dupli)
        remove_dupli=[i for i in remove_dupli if not 'youtube' in i and not '.svg' in i and not '.png' in i and not '.mp3' in i and not '.mp4' in i and not '@' in i and not 'privacy' in i]
       # print(remove_dupli)
        if(len(remove_dupli)!=0):
            for x in remove_dupli:
                status=check_whether_job(x)
                if(status):
                    out=get_all_jobs(x,url,remove_dupli)
                    for each_job in out:
                        add_all_jobs.append(each_job)
                    break
        print("No anchor link is a job")
        
    except:
        pass


def get_job(url):
    out=''
    store_first_keyword=''
    company_name=url
    if(check_whether_job(company_name)):
        out=company_name
    print("given url is not a job")
    if(out==''):    
        try:
            browser.get(url)
            time.sleep(1)
            alllinks = []
            innerHTML=browser.execute_script('return document.body.innerHTML')
            iframes = browser.find_elements_by_tag_name('iframe')
            no_of_iframes = len(iframes)
            if(no_of_iframes > 0):
                for i in range(0, len(iframes)):
                    try:
                        f = browser.find_elements_by_tag_name('iframe')[i]
                        browser.switch_to.frame(i)
                        elems = browser.find_elements_by_xpath("//a[@href]")
                        for uma in elems:
                            try:
                                if (uma.text != ''):
                                    store_both = {"url": uma.get_attribute('href'), "label": uma.text.replace("\n", " ") + "+-"}
                                    alllinks.append(store_both)
                            except:
                                pass
                        browser.switch_to_default_content()
                    except:
                        pass
            links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', innerHTML)
            for link in links:
                try:
                    linktext = str(link).replace("&quot;);", "")
                    linktext = linktext.rstrip('/')
                    linktext = linktext.split('/')[-1]
                    linktext = linktext.replace('-',' ').replace('\n',' ').title()
                    link_label_json = {'url': link, 'label': linktext}
                    alllinks.append(link_label_json)
                except:
                    pass
            elems = browser.find_elements_by_xpath("//a[@href]")
            get_anchors=[]
            add=[]
            get_links=[]
            for uma in elems:
                try:
                    if(uma.text!=''):
                        store_both = {"url": uma.get_attribute('href'), "label": uma.text.replace("\n"," ")+"+-"}
                        alllinks.append(store_both)
                except:
                    pass
            for i in alllinks:
                get_anchor=i['label'].replace('+-','').strip()
                if(get_anchor.isdigit()==True and len(get_anchor)<=3):
                    get_links.append(i['url'])
            get_links=set(get_links)
            get_links=list(get_links)
            if(len(get_links)>0):
                iterateAnchors(get_links)
            print(set(add_all_jobs))
            exit(0)
            add=json.dumps(alllinks)
            data = {
                'labelitems': add
                }
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
            }
            try:
                response = requests.post('http://ijiraq.dev.bigml.com/identify/label/jobtitle',  data=data,headers=headers).json()
                print("Got anchor links of a page")
                remove_dupli=[]
                for i in response:
                    if((i['confidence']*100)>60):
                        remove_dupli.append(i['url'])
                remove_dupli=set(remove_dupli)
                remove_dupli=[i for i in remove_dupli if not 'youtube' in i and not '.svg' in i and not '.png' in i and not '.mp3' in i and not '.mp4' in i and not '@' in i and not 'privacy' in i]
               # print(remove_dupli)
                if(len(remove_dupli)!=0):
                    for x in remove_dupli:
                        status=check_whether_job(x)
                        if(status):
                            out=get_all_jobs(x,url,remove_dupli)
                            for each_job in out:
                                add_all_jobs.append(each_job)
                            break
                print("No anchor link is a job")
            except:
                pass
            if(out==''):
                anchor_match_words=["positions",
                        "opportunities",
                        "openings",
                        "jobs",
                        "job board",
                        "careers",
                        "employment",
                        "job search",
                        "apply now",
                        "search",
                        "vacancies"]
                browser.get(company_name)
                time.sleep(2)
                flag=1
                print("Going to logic to click")
                out=logic_to_click(company_name,flag,anchor_match_words)

        except TimeoutException as e:
            print()
            print("Page load Timeout Occured. Quiting !!!")
            browser.quit()

    return(out)


def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False


def to_naviagte():
    return_val='no change'
    try:
        if(len(browser.window_handles[-1])):
            browser.switch_to_window(browser.window_handles[-1])
            return_val=browser.current_url
            browser.switch_to_window(browser.window_handles[0])
    except:
        pass
    return(return_val)


def check_whether_job(url):
    text_content=''
    text_content_iframe=''
    data=''
    get_text_len=''
    get_text_content=[]
    iframe_content_len=0
    if("pdf" in url):
        try:
            r = requests.get(url, stream=True)
            with open('d://python//created_pdf.pdf', 'wb') as f:
                f.write(r.content)
            pdfFileObj = open('created_pdf.pdf', 'rb') 
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
            page_content=''
            no_of_pages=pdfReader.numPages
            if(no_of_pages==1):
                pageObj = pdfReader.getPage(0)
                page_content=pageObj.extractText()
                 
            if(no_of_pages>=2):
                for i in range(0,2):
                    pageObj = pdfReader.getPage(i) 
                    page_content+=pageObj.extractText()
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            }
            data = {
            'jobbody': page_content.encode('utf-8')
            }
            response = requests.post('http://ijiraq.dev.bigml.com/predict/page', headers=headers, data=data)
            data=json.loads(response.content)
            if((data['page_check']*100)>=60):
                return True
            else:
                return False
        except:
            return False
    
    
    if(is_url(url)):
        get_text_len=[]
        try:
            browser.get(url)
            time.sleep(1)
            html=browser.find_elements_by_xpath('//html')
            if(len(html)>=1):
                text_content=browser.find_element_by_xpath('//html').text
            original_content_len=len(text_content)
            iframes = browser.find_elements_by_tag_name('iframe')
            no_of_iframes = len(iframes)
            if(no_of_iframes > 0):
                try:
                    for i in range(0, len(iframes)):
                        try:
                            browser.switch_to.frame(i)
                            text_content_iframe=browser.find_element_by_xpath('//html').text
                            get_text_len.append(len(text_content_iframe))
                            iframe_content_len=max(get_text_len)
                        except:
                            pass
                except:
                    pass
            if(iframe_content_len<=original_content_len):
                text_content=text_content
            else:
                text_content=text_content_iframe
            prediction = deepnet.predict({'field1': text_content}, full = True)
            try:
                if(int(prediction['prediction'])==1 and (prediction['probability']*100)>=60 and 'about' not in url and'www.w3.org' not in url and 'policy' not in url and "schema.org" not in  url ):
                    return True
                else:
                    return False

            except:
                pass

        except TimeoutException as e:
            print()
            print("Page load Timeout Occured. Quiting !!!")
            browser.quit()


    else:
        return False


def check_for_alert():
    try:
        alert = browser.switch_to.alert
        alert.accept()
    except:
        pass


def logic_to_click(company_name,flag,anchor_match_words):
    out=''
    get_name=''
    entered=0
    ##print(company_name)
    get_name=company_name.rsplit('/', 1)[-1]
    if(get_name==''):
        get_name=company_name.rsplit('/', 1)[-2]
        get_name=get_name.rsplit('/', 1)[-1]
    print("Checking all logics to click")
    check_for_alert()
    elem=browser.find_elements_by_xpath("//a[@href]")
    try:
        for i in range(len(elem)-1,0,-1):
            cleanr = re.compile('<.*?>')
            anchor_text = re.sub(cleanr,'',elem[i].get_attribute('innerHTML') )
            for word in anchor_match_words :
                if((word.strip().lower() in anchor_text.strip().lower() and anchor_text!='' and get_name.lower()!=word)):
                    out=elem[i].get_attribute("href")
                    browser.get(elem[i].get_attribute("href"))
                    anchor_match_words.remove(word)
                    entered=1
                    break
            if(out!=''):
                break
        
    except:
        pass
    check_for_alert()
    if(entered==0):
        elem=browser.find_elements_by_xpath('''//a[@onclick]''')
        if(len(elem)>=1):
            try:
                for i in elem:
                    cleanr = re.compile('<.*?>')
                    anchor_text = re.sub(cleanr,'',i.get_attribute('innerHTML') )
                    anchor_match_words_1=["positions",
                                        "opportunities",
                                        "openings",
                                        "jobs",
                                        "employment",
                                        "careers",
                                        "apply now",
                                        "job search",
                                        "search",
                                        "vacancies"]
                    for word in anchor_match_words_1 :
                        if(word in anchor_text.strip().lower() and anchor_text!=''):
                            i.click()
                            entered=1
                            out=browser.current_url
                            break
                    if(out!=''):
                        break
            except:
                pass
    check_for_alert()
    if(entered==0):
        elem=browser.find_elements_by_xpath("//input[@type='submit']")
        if(len(elem)>=1):
            for i in elem:
                try:
                    current_url=browser.current_url
                    insert_text_in_textBox()
                    i.click()
                    nav_val=to_naviagte()
                    if(nav_val=='no change'):
                        out=browser.current_url
                    else:
                        out=nav_val
                    check_for_alert()
                except:
                    pass
    check_for_alert()
    current_url=browser.current_url
    if current_url == company_name and entered==0 :
        elem=browser.find_elements_by_xpath("//button[@type='submit']")
        if(len(elem)>=1):
            for i in elem:
                try:
                    current_url=browser.current_url
                    i.click()
                    nav_val=to_naviagte()
                    if(nav_val=='no change'):
                        out=browser.current_url
                    else:
                        out=nav_val
                    check_for_alert()
                except:
                    pass
    check_for_alert()
    current_url=browser.current_url
    if current_url == company_name and entered==0 :
        elem=browser.find_elements_by_xpath("//input[@type='image']")
        if(len(elem)>=1):
            try:
                for i in elem:
                    current_url=browser.current_url
                    i.click()
                    nav_val=to_naviagte()
                    if(nav_val=='no change'):
                        out=browser.current_url
                    else:
                        out=nav_val
                    check_for_alert()
            except:
                pass
    check_for_alert()
    current_url=browser.current_url
    if current_url == company_name and entered==0 :
        elem=browser.find_elements_by_xpath("//button[@type='button']")
        if(len(elem)>=1):
            for i in elem:
                try:
                    current_url=browser.current_url
                    i.click()
                    nav_val=to_naviagte()
                    if(nav_val=='no change'):
                        out=browser.current_url
                    else:
                        out=nav_val
                    check_for_alert()
                except:
                    pass
    check_for_alert()
        
    final_out=''
    if(out=='' ):
        final_out='No job link'
    
    else:
        try:
            browser.get(out)
            print("fetching anchor links")
            time.sleep(1)
            innerHTML=browser.execute_script('return document.body.innerHTML')
            links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', innerHTML)
            alllinks=[]
            iframes = browser.find_elements_by_tag_name('iframe')
            no_of_iframes = len(iframes)
            if(no_of_iframes > 0):
                for i in range(0, len(iframes)):
                    try:
                        f = browser.find_elements_by_tag_name('iframe')[i]
                        browser.switch_to.frame(i)
                        elems = browser.find_elements_by_xpath("//a[@href]")
                        for uma in elems:
                            try:
                                if (uma.text != ''):
                                    store_both = {"url": uma.get_attribute('href'), "label": uma.text.replace("\n", " ") + "+-"}
                                    alllinks.append(store_both)
                            except:
                                pass
                        browser.switch_to_default_content()

                    except:
                        pass
            for link in links:
                try:
                    linktext = str(link).replace("&quot;);", "")
                    linktext = linktext.rstrip('/')
                    linktext = linktext.replace('-',' ').replace('\n',' ').title()
                    link_label_json = {'url': link, 'label': linktext}
                    alllinks.append(link_label_json)
                except:
                    pass
            elems = browser.find_elements_by_xpath("//a[@href]")
            get_anchor=[]
            add=[]
            for uma in elems:
                try:
                    if(uma.text!=''):
                        store_both = {'url': uma.get_attribute('href'), 'label': uma.text.replace("\n"," ")+'+-'}
                        alllinks.append(store_both)
                except:
                    pass
            add=json.dumps(alllinks)
            data = {
                'labelitems' : add
            }
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
            }
            try:
                response = requests.post('http://ijiraq.dev.bigml.com/identify/label/jobtitle',  data=data,headers=headers).json()
                remove_dupli=[]
                for i in response:
                    if((i['confidence']*100)>60):
                        remove_dupli.append(i['url'])
                remove_dupli=set(remove_dupli)
                print("Getting anchor tags of a page")
                remove_dupli=[i for i in remove_dupli if not 'youtube' in i and not '.svg' in i and not '.png' in i and not '.mp3' in i and not '.mp4' in i and not '@' in i and not 'privacy' in i]
                if(len(remove_dupli)!=0):
                    for x in remove_dupli:
                        status=check_whether_job(x)
                        if(status):
                            final_out=get_all_jobs(x,url,remove_dupli)
                            for each_job in final_out:
                                add_all_jobs.append(each_job)
                            break
                print("No job in anchor tags")
            except:
                pass

            if(final_out==''):
                for i in range(0,len(alllinks)):
                    list_.append(alllinks[i]["label"])
                try:
                    rep_val=statistics.mode(list_)
                except:
                    rep_val='no value'

                for i in alllinks:
                    if(rep_val==i['label']):
                        if(check_whether_job(i['url'])):
                            final_out=i['url']
                        break
                if(final_out==''):
                    final_out='No job link'
               
            if(final_out=='No job link'):
                if(flag==1 or flag==2):
                    if(flag==1):
                        flag=2
                    else:
                        flag=0
                    browser.get(out)
                    time.sleep(1)
                    print("For next click")
                    final_out=logic_to_click(out,flag,anchor_match_words)
        
        except TimeoutException as e:
            print()
            print("TimeoutException")
            browser.quit()

    return(final_out)


options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome('D://chromedriver.exe',chrome_options=options)
browser.maximize_window()
browser.set_page_load_timeout(500)
# query=collection.find({'Status':0})
# for i in query:
#     myquery = { "Url": i['Url'] }
#     newvalues = { "$set": { "Jobs":get_job(i['Url']) ,'Status':1}}
#     collection.update_many(myquery, newvalues)
print('End urls : '+str(get_job(input('Enter the url : '))))
browser.quit()
