import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymongo
from selenium.webdriver.support.ui import Select
from pymongo import MongoClient, DESCENDING
client = MongoClient("mongodb://localhost:27017/basics")
if(client):
    print("connected")
db = client.Appcast
collections = db.sanofi
options = webdriver.ChromeOptions()
preferences = {'profile.default_content_setting_values': { 'images': 2,}}
options.add_experimental_option('prefs', preferences)
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
driver.get("http://cipherfolks.com/old_hrms/")
time.sleep(1)
driver.find_element_by_xpath('//input[@id="iusername"]').send_keys('fionagrace')
driver.find_element_by_xpath('//input[@id="ipassword"]').send_keys('fgrace$$##')
driver.find_element_by_xpath('//button[@class="btn btn-primary btn-block btn-flat save"]').click()
'''window_before = driver.window_handles[0]
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
time.sleep(2)'''
#driver.get('http://cipherfolks.com/old_hrms/admin/employees')
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(), 'Staff')]").click()
driver.find_element_by_xpath("//a[contains(text(), ' Employees')]").click()
driver.find_element_by_xpath('//button[@class="btn btn-xs btn-primary"]').click()
time.sleep(1)
name='manoj'
email='manoj@gmail.com'
passowrd='123456'
driver.find_element_by_xpath('//input[@name="first_name"]').send_keys(name)
driver.find_element_by_xpath('//input[@name="last_name"]').send_keys(name)
#driver.find_element_by_xpath('//span[@id="select2-department_id-dt-container"]').click()
#driver.find_element_by_xpath('//li[@id="select2-aj_subdepartments-result-w3ch-3"]').click()
driver.find_element_by_xpath('//input[@name="username"]').send_keys('name')
driver.find_element_by_xpath('//input[@name="email"]').send_keys(email)
#company
driver.find_element_by_xpath('//span[@id="select2-aj_company-container"]').click()
driver.find_element_by_xpath('//li[@class="select2-results__option select2-results__option--highlighted"]').click()
#dob picker
bday=driver.find_element_by_xpath('//input[@class="form-control date_of_birth hasDatepicker"]')
driver.execute_script("arguments[0].removeAttribute('readonly')", bday);
bday.send_keys("2018-08-03")
#joning
sb_dt = driver.find_element_by_xpath('//input[@class="form-control date_of_joining hasDatepicker"]')
driver.execute_script("arguments[0].removeAttribute('readonly')", sb_dt);
sb_dt.send_keys("2018-08-03")
driver.find_element_by_xpath('//input[@name="contact_no"]').send_keys('7893251866')
driver.find_element_by_xpath('//input[@name="employee_id"]').send_keys(name)
driver.find_element_by_xpath('//input[@name="password"]').send_keys(passowrd)
driver.find_element_by_xpath('//input[@name="confirm_password"]').send_keys(passowrd)
time.sleep(2)
#department
driver.find_element_by_xpath('//span[contains(text(), "Department")]').click()
driver.find_element_by_xpath('//li[contains(text(), "BPO")]').click()
#sub-deppartment

sub_dt = driver.find_element_by_xpath('span[contains(text(), "Select Department")]').click()
driver.execute_script("arguments[0].removeAttribute('readonly')", sb_dt);
sub_dt.send_keys("Customer Support Executive")
#driver.find_element_by_xpath('//li[contains(text(), "Customer Support Executive")]').click()
#designation
driver.find_element_by_xpath('//span[contains(text(), "Designation")]').click()



#driver.find_element_by_xpath('//input[@class="form-control date_of_joining hasDatepicker"]').send_keys('2019-07-03')
#select = Select(driver.find_element_by_xpath('//span[@id="select2-aj_company-container"]'))
#select.select_by_index(0)
#print("Page Title is : %s" %driver.title)
#driver.find_element_by_xpath("//input[@class='textboxdata hasDatepicker' and @id='date']").send_keys("10-04-2018")


