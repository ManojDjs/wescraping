from lxml import etree as ET
# import xml.etree.ElementTree as ET
from pymongo import MongoClient
from unidecode import unidecode
from datetime import date
# import lxml.html
import re
import html
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
try:
    # Local database connection
	# conn = MongoClient()
	# db = conn.appCast
	# collection = db.appCastDistinctTitle
    # server connection
	# dbname 		= "stage_jobiak_ai"
	# mongoUrl	= 'mongodb://'+ 'stagejob' +':'+ 'St%40gej0b%40i' +'@' +"18.223.47.109"+':'+str('28015')+'/'+dbname
	# client 		= MongoClient(mongoUrl)
	# collection 	= client[dbname]['company-urls9']
    # server connection
    dbname = "stage_jobs"
    mongoUrl = 'mongodb://admin:jobiak@3.18.238.8:28015/admin'
    client = MongoClient(mongoUrl)
    collection = client[dbname]['project']
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# create the file structure
data = ET.Element('root')
# labels = ET.SubElement(data, 'jobs')
today = str(date.today())

# alldata = collection.find({"$or":[{"TStatus" : 3},{"TStatus":2}],"locationGoogleStatus":True, "jobDescriptionString":{"$exists":True}, "postedDate":{"$exists":True}} )

# alldata = collection.find({"$or":[{"TStatus" : 3},{"TStatus":2}],"locationGoogleStatus":True, "jobDescriptionString":{"$exists":True}} )

alldata = collection.find({"jobDescriptionString": {"$exists": True},'Recheck':3})
alldata_count = collection.count_documents({"jobDescriptionString": {"$exists": True},'Recheck':3})

# alldata = collection.find({"$or":[{"TStatus" : 3},{"TStatus":2}]} )

print('Total record found: ' + str(alldata_count))

# exit()
counter = 1
for elm in alldata:
    print('Processing element no # ' + str(counter) + '   ID: ' + str(elm['_id']))
    label1 = ET.SubElement(data, 'row')

    # database values
    title = ''
    if elm['title']:
        title = str(elm['title'])

    # print(elm['locationGoogleStatus'])

    if 'locationGoogleStatus' in elm:
        if elm['locationGoogleStatus'] == True:
            location = str(elm['predictionValue'])
        else:
            location = str(elm['location'])
    else:
        location = location = str(elm['location'])
    # if elm['locationGoogleStatus'] == True:
    #	location = str(elm['predictionValue'])
    # else:
    #	location = str(elm['location'])
    company = str(elm['company'])
    postedDate = today
    '''if elm['postedDate'] == None:
		postedDate = today		
	else:
		postedDate = str(elm['postedDate'])	'''
    if elm['jobDescriptionString']:
        # jobDescriptionString =   str(elm['jobDescriptionString']).replace('\f',' ')
        # jobDescriptionString = lxml.html.tostring(elm['jobDescriptionString'])
        # jobDescriptionString = elm['jobDescriptionString'].replace("&amp;", "&")
        jobDescriptionString = re.sub(u"[^\x20-\x7f]+", u"", elm['jobDescriptionString'])
    # jobDescriptionString = BeautifulSoup(jobDescriptionString)
    if 'expirationDate' in elm:
        if elm['expirationDate'] == None:
            expirationDate = ""
        else:
            expirationDate = str(elm['expirationDate'])
    else:
        expirationDate = ""
    # if elm['expirationDate'] == None:
    # 	expirationDate = ""
    # else:
    # 	expirationDate = str(elm['expirationDate'])
    if 'jobId' in elm:
        if elm['jobId'] == None:
            jobId = ""
        else:
            jobId = ""
    else:
        jobId = ""
    if 'city' in elm:
        if elm['city']==None:
            city=""
        else: city=str(elm['city'])
    else:
        city=''

    if 'country' in elm:
        if elm['country']==None:
            country=""
        else: country=str(elm['country'])
    else:
        country=''
    if 'state' in elm:
        if elm['state']==None:
            state=""
        else: state=str(elm['state'])
    else:
        state=''
    if 'zipCode' in elm:
        if elm['zipCode']==None:
            zipCode=""
        else: zipCode=str(elm['zipCode'])
    else:
        zipCode=''


    # if elm['jobId'] == None:
    # 	jobId = ""
    # else:
    # 	jobId = str(elm['jobId'])
    if 'jobType' in elm:
        if elm['jobType'] == None:
            jobType = ""
        else:
            jobType = str(elm['jobType'])
    else:
        jobType = ""
    # if elm['jobType'] == None:
    # 	jobType = ""
    # else:
    # 	jobType = str(elm['jobType'])
    if 'salary' in elm:
        if elm['salary'] == None:
            salary = ""
        else:
            salary = str(elm['salary'])
    else:
        salary = ""
    # if elm['salary'] == None:
    # 	salary = ""
    # else:
    # 	salary = str(elm['salary'])

    link = elm['url']

    # assigning to label
    item1 = ET.SubElement(label1, 'job_title')
    item1.text = title

    item2 = ET.SubElement(label1, 'job_location')
    item2.text = location

    item3 = ET.SubElement(label1, 'Company')
    item3.text = company

    item4 = ET.SubElement(label1, 'Date_posted')
    item4.text = postedDate

    item5 = ET.SubElement(label1, 'job_description')
    item5.text = html.unescape(jobDescriptionString)

    # item6 	= ET.SubElement(label1, 'validThrough')
    # item6.text = expirationDate

    item7 = ET.SubElement(label1, 'Jobid')
    item7.text = jobId

    # item8 	= ET.SubElement(label1, 'jobType')
    # item8.text = jobType

    item9 	= ET.SubElement(label1, 'job_salary')
    item9.text = salary
    item10 = ET.SubElement(label1, 'Joburl')
    item10.text = link
    item11 = ET.SubElement(label1, 'city')
    item11.text = city
    item12 = ET.SubElement(label1, 'job_country')
    item12.text = country
    item13 = ET.SubElement(label1, 'job_state')
    item13.text = state
    item14 = ET.SubElement(label1, 'zipCode')
    item14.text = zipCode

    counter = counter + 1

# create a new XML file with the results
mydata = ET.tostring(data, encoding="utf-8", method="xml", pretty_print=True, xml_declaration=True)
myfile = open("monster-data.xml", "wb")
myfile.write(mydata)
