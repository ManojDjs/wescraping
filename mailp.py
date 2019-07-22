from flask import Flask,jsonify
from flask import request
import json
import requests
app =Flask(__name__)
@app.route('/datas',methods=['Post'])
def adddata():
    return('manoj')

if __name__ == '__main__':
   app.run(debug = True, port="5000")