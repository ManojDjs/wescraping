import lxml.html
import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
l=['div','p','a','b','body']
firststing=[]
for i in range(0,len(l)-1):
    p=soup.find(l[i],string="The Dormouse's story")
    if p is not None:
        firststing.append(p)
        print(p.find_parents("l[i])"))
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(firststing)

fs=str(firststing[0])
tag=fs[1:2]
print(fs)
print(firststing[0].find_all_next(tag))

