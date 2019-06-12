from selenium import webdriver
import re
import  time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("D:\Office_Files\chromedriver.exe")
driver.get('https://web.whatsapp.com/')
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]').send_keys('hai')
driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]').click()
#print(driver.execute_script(return arguments[0].innerHTML", te
time.sleep(10)
