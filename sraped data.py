from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("D:\Office_Files\chromedriver.exe")
driver.get("https://jobs-willamettedental.icims.com/jobs/8988/marketing-communications-specialist/job?iis=Appcast&mobile=false&width=958&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330")
print(driver.title)
print(driver.current_url)
iframes = driver.find_elements_by_tag_name('iframe')
no_of_iframes = len(iframes)
if(no_of_iframes > 0):
    try:
        for i in range(0, len(iframes)):
            try:
                driver.switch_to.frame(i)
                text = driver.find_element_by_xpath("//div[@class='iCIMS_JobContent']")
                k=text.get_attribute('innerHTML')
                #k=driver.execute_script("return arguments[0].outerHTML", k)
            except:
                pass
    except:
        pass
else:
    text = driver.find_element_by_xpath("//div[@class='iCIMS_JobContent']")
    k=text.get_attribute('innerHTML')
def cleanhtml(raw_html):
 cleanr = re.compile('<.*?>')
 cleantext = re.sub(cleanr, '', raw_html)
 return cleantext
print(cleanhtml(k))
#print(driver.execute_script("return arguments[0].innerHTML", text))
driver.quit()


