from selenium import webdriver
from pyvirtualdisplay import Display
from flask import Flask,request,Response,make_response,jsonify
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
app=Flask(__name__)
@ app.route('/data',methods=['GET'])
def call():
   url = request.args.get('url')
   goturl=url
   innerHTML=''
   b=''
   try:
           display = Display(visible=0, size=(1024, 768))
           display.start()
           firefoxProfile = FirefoxProfile()
           firefoxProfile.set_preference('permissions.default.stylesheet', 2)
           firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')
           firefoxProfile.set_preference('permissions.default.image', 2)
           browser = webdriver.Firefox(firefoxProfile)
           browser.delete_all_cookies()
           browser.get(goturl)
           b=browser.title
           print(b)
   finally:
           browser.quit()
           display.stop()
   headers={ 'content-type':'text/plain; charset=utf8' }
   response = make_response(innerHTML,200)
   response.headers = headers
   return(b)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)

