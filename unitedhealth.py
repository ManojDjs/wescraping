element=driver.find_elements_by_xpath('//tbody/tr[@class="data-row clickable"]')
for i in element:
                print(i.text)
