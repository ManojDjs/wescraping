from difflib import SequenceMatcher
from pymongo import MongoClient
client = MongoClient('mongodb://jobiak:j0Bi%40kSt%40ge@18.223.47.109:28015/stage_jobs')
if(client): print("connected")
db = client.stage_jobs
def similar(a, b):return SequenceMatcher(None, a, b).ratio()
def titlepercentage(matched,count): return ((matched/count)*100)
def locationpercentage(matched,count): return ((matched/count)*100)
def companypercentage(matched,count): return ((matched/count)*100)
def jobDescriptionpercentage(matched,count): return ((matched/count)*100)
collections = db.five_links_fetch_data
collections2=db.dataFromFiveLinksFetchData
totalcount=0
matchedrows=0
titlecount=0
locationcount=0
companycount=0
jobDescriptioncount=0
querymatches=0
for x in collections.find({'Link':{'$ne':''},'updateStatus':1}).skip(1500):
    querymatches=querymatches+1
    print("-------------------------------------------------------------------------------------------------------")
    print('********************************************************************')
    print('     *************    QUERY MATCH NO:-->>'+str(querymatches)+'     ***************')
    print('********************************************************************')
    print(x['Link'])
    try:
        y=collections2.find_one({'Link':x['Link']})

        print('Match NO---------->>>>>>>>>'+str(totalcount))
        print(y['Link'])
        t1=x['title']
        print(t1)
        t2=y['title']
        print(t2)
        location1=x['location']
        print(location1)
        location2=y['location']
        print(location2)
        company1=x['company']
        print(company1)
        company2=y['company']
        print(company2)
        jobDescription=x['jobDescriptionString']
        print('----------->>>>>>>>>>>>>Descrptipn 1')
        print(jobDescription)
        jobDescription2=y['jobDescriptionString']
        print('----------->>>>>>>>>>>>>Descrptipn 2')
        print(jobDescription2)
        titlematch1=similar(t1,t2)
        print(titlematch1)
        locationmatch2=similar(location1,location2)
        print(locationmatch2)
        companymatch3=similar(company1,company2)
        print(companymatch3)
        jobDescriptionmatch4=similar(jobDescription,jobDescription2)
        print(jobDescriptionmatch4)
        totalcount=totalcount+1
        if titlematch1==1:
            print('title percentage ')
            titlecount=titlecount+1
            print(titlepercentage(titlecount,totalcount))
        if locationmatch2==1:
            print('location percent')
            locationcount=locationcount+1
            print(locationpercentage(locationcount,totalcount))
        if companymatch3==1:
            print('company percent')
            companycount=companycount+1
            print(companypercentage(companycount,totalcount))
        if jobDescriptionmatch4>0.7:
            jobDescriptioncount=jobDescriptioncount+1
            print(jobDescriptionpercentage(jobDescriptioncount,totalcount))
        if(titlematch1==1 and locationmatch2==1 and companymatch3==1):
            matchedrows=matchedrows+1
            print(matchedrows)
            print((matchedrows/totalcount)*100)

    except:
        print('no element found')
print('--------->>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<----------')
print('FINAL REPORT OF MATCHING PERCENTAEGE')
print('TOTAL MATCHES FOUND :'+str(totalcount))

print('INDIVIDUAL TITLE PERCENTAGE:')
print('TITLES MATCHED ARE------>>>>'+str(titlecount))
print(titlepercentage(titlecount,totalcount))

print('INDIVIDUAL LOCATION PERCENTAEG:')
print('LOCATION MATCHED ARE---->>>>'+str(locationcount))
print(locationpercentage(locationcount,totalcount))

print('INDIVIDUAL COMPANY PERCENTAGE')
print('COMPANIES MATCHED------->>>>'+str(companycount))
print(companypercentage(companycount,totalcount))

print('JOB DESCRIPTION MATCH PERCENTAGE WHICH ARE GREATER THAN 70')
print(jobDescriptionpercentage(jobDescriptioncount,totalcount))

print('TOTAL 3, TITLE, LOCATION AND COMPANY PERCENTAGES INCLUDED')
print((matchedrows/totalcount)*100)

print('--------->>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<----------')
