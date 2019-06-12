import time
from selenium import webdriver
import pymongo
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient, DESCENDING
from flask import Flask, jsonify
from werkzeug.utils import redirect
import requests
import  request
from pymongo import MongoClient
app = Flask(__name__)
@app.route('/success/<string:name>',methods = ['POST', 'GET'])
def success(name):
        l= request.get('language')
        #options.add_argument("--disable-extensions")
        return l
if __name__ == '__main__':
    app.run(port=3808)
