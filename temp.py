from pymongo import MongoClient

import requests
from pymongo import MongoClient
from flask import Flask, redirect, url_for, request
from requests.utils import requote_uri
import time

start_time = time.time()
app = Flask(__name__)
import re

if (1 == 1):
    dbname1 = "stage_jobs"
    dbname2 = "stage_jobiak_ai"
    mongoUrl1 = 'mongodb://' + 'jobiak' + ':' + 'j0Bi%40kSt%40ge' + '@' + "18.223.47.109" + ':' + str(
        '28015') + '/' + dbname1
    client1 = MongoClient(mongoUrl1)
    collection1 = client1[dbname1]['appCast_Skills_1']
    collection2 = client1[dbname1]['ALL_IYS_DICE_FINAL']

    print("Connected successfully!!!")
    mydoc1 = collection1.find({'Status':200}, no_cursor_timeout=True).skip(1).limit(1000)
    mydoc2 = collection2.find({}, no_cursor_timeout=True)
    skillset1 = []
    skillset2 = []
    for y in mydoc2:
        if (len(y['Skill_name']) > 5):
            skillset1.append(" " + y['Skill_name'] + " ")
        else:
            skillset2.append(y['Skill_name'])
    print("--- Skills Stored:::::%s seconds ---" % (time.time() - start_time))
    S1 = set(skillset2)
    matchedskillset = [];
    pm = 0
    for x in mydoc1:
        if (isinstance(x["body"], str)):
            pm = pm + 1
            print(pm)
            print(x["body"])
            print(type(x["body"]))
            print("\n")
            x["body"] = " " + x["body"] + " "
            x["body"] = re.sub(r'[^a-zA-Z0-9-\s]+', ' ', x["body"])
            print(x["body"])
            S2 = set(x["body"].split())
            data1 = S2.intersection(S1)
            for word in skillset1:
                if word in x['body']:
                    data1.add(word)
                else:
                    if word.lower() in x['body'].lower():
                        data1.add(word)
            data1 = list(data1)
            data1.sort(key=lambda x: len(x))
            for i in range(0, len(data1)):
                skill = data1[i]
                for j in range(i + 1, len(data1)):
                    # print(skill+":::"+data1[j])
                    # maindata=data1[j].split()
                    if skill.lower() in data1[j].lower():
                        data1[i] = None
            data1 = list(filter(None, data1))
            data1.sort(key=lambda x: len(x))
            maindata = []
            for skill in data1:
                maindata.append(skill.strip())
            maindata.sort(key=lambda x: len(x))
            print("\n")
            print(list(set(maindata)))
            print("\n")
            # SKILL SET FROM body
            import datetime
            now = datetime.datetime.now()
            URL = "http://ijiraq.dev.bigml.com:8443/recommend/skill/title/?"
            for seed in maindata:
                URL = URL + "&seed=" + seed
            r = requests.get(url=URL)
            data = r.json()
            print("------------API Responses-------------")
            print(data)
            print(URL)
            print("----------------------------------------")
            i = 0
            separatorset = []
            for TitlesAPI in data['recommendations']:
                separatorset.append(TitlesAPI['value'])
                i = i + 1;
                if (i == 5):
                    break;
                print(TitlesAPI['value'])
                print("\n")

            collection1.update_one({"_id": x['_id']}, {
                "$set": {"SKILL-SET-NEW": str(maindata), "Status":143, "UpdateTime": now.strftime("%Y-%m-%d %H:%M:%S"),
                         'APIResponse-NEW': str(data), 'TopTitle-NEW': separatorset}})
    print("--- Total Time Taken %s seconds ---" % (time.time() - start_time))
    print("\n")

