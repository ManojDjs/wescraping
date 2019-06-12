import lxml.html
import requests
from lxml import etree
import xml.etree.ElementTree as ET
from io import StringIO, BytesIO
from xml.dom import minidom
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

con = MongoClient('localhost', 27017)
db = con['Url_data']
collection = db['GetDescSample']


def findEndString(root, endString):
    cleanr = re.compile('<.*?>')
    for i in root.iter():
        try:
            textOutOfTheTag = re.sub(cleanr, '', str(ET.tostring(i)))
            if (endString in i.text or endString in textOutOfTheTag):
                return True
        except:
            pass
    # #print(i.text)
    # print()

    return False


def traverseToGetParent(parent, root):
    for i in root.iter():
        try:
            if (ET.tostring(i) == ET.tostring(parent)):
                return (i.getparent())
        except:
            pass
        # print("Entered In except")
    return "Empty"


def appendParent(count):
    topparentNode = 'i.getparent()'
    print("We came here")
    for i in range(0, count - 1):
        topparentNode = topparentNode + '.getparent()'
    print(topparentNode)
    return (topparentNode)


def getEndParent(root, endString):
    for i in root.iter():
        try:
            if (endString in i.text):
                endparentNode = i.getparent()
                print(i.getparent())
                endText = i.text
                endTag = i.tag
                print("Node : " + i.text)
                print("Tag : " + i.tag)
        except:
            pass

    return (endparentNode, endTag, endText)


url = input("Enter Job url : ")
html = requests.get("http://18.221.95.143:8015/?url=" + url)

string = html.content.decode("utf-8")
print(type(string))

soup = BeautifulSoup(string, 'lxml')
[s.extract() for s in soup(['script', 'font', 'head', 'meta', 'style'])]
parser = etree.XMLParser(recover=True)
root = etree.fromstring(str(soup), parser=parser)

# topString='Do you describe yourself as highly detailed and process oriented'
# endString='EOE'
topString = input('Enter start of the desc.. : ')  # 'Licensed Real Estate Sales Agent'
endString = input('Enter end of the desc.. : ')  # 'potential employees with the same level of care and respect'
endTag = ''
endText = ''

# for i in root.iter():
# 	try:
# 		print()
# 		print(i.tag)
# 		print(i.attrib)
# 		print(i.text)
# 		print()
# 	except:
# 		pass
# exit(0)

cleanr = re.compile('<.*?>')

for i in root.iter():
    try:
        textOutOfTheTag = re.sub(cleanr, '', str(ET.tostring(i)))
        # print(textOutOfTheTag)
        if (topString in i.text or topString in textOutOfTheTag):
            topText = i.text
            topTag = i.tag
            print("Node : " + i.text)
            print("Tag : " + i.tag)
            topparentNode = i.getparent()
            for j in range(1, 20):
                print(j)
                print(topparentNode.attrib)
                print(findEndString(topparentNode, endString))

                if (findEndString(topparentNode, endString) == True):
                    with open('C://Users//behar//Desktop//gotDEsc.txt', 'w', encoding='utf-8') as f:
                        f.write(ET.tostring(topparentNode).decode('utf-8'))
                    exit(0)

                if ~findEndString(topparentNode, endString):
                    topparentNode = traverseToGetParent(topparentNode, root)
                # print(topparentNode.attrib)

                print('--')
    except:
        pass

exit(0)
endparentNode, endTag, endText = getEndParent(root, endString)
print()
print(topText)
print(endparentNode)
print(endText)
