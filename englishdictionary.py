import pymongo
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/<string:word>')
def dict(word):
    from pymongo import MongoClient, DESCENDING
    from selenium import webdriver
    import re
    from selenium.webdriver.common.keys import Keys
    client = MongoClient("mongodb://localhost:27017/")
    if client:
        print("connected")
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                    'plugins': 2, 'popups': 2, 'geolocation': 2,
                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                    'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                    'durable_storage': 2}}
        options.add_experimental_option('prefs', prefs)
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        #driver = webdriver.Chrome("D:\Office_Files\chromedriver.exe")
        driver = webdriver.Chrome(chrome_options=options, executable_path=r'D:\Office_Files\chromedriver.exe')
        driver.get("https://dictionary.cambridge.org/dictionary/")
        ele = driver.find_element_by_class_name("cdo-search__input")
        ele.send_keys(word)
        driver.find_element_by_class_name('cdo-search__button').click()
        meaning = driver.find_element_by_xpath("//p[@class='def-head semi-flush']/b[@class='def']").text
        return(meaning)
        driver.close()
if __name__ == '__main__':
 app.run(debug = True,port=5000)
