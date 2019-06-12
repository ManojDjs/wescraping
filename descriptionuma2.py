import requests
import json
import re
url=input('Enter url : ')
response = requests.get("http://35.167.157.151:8021/?Url="+url).json()
diffBotDesc = ''
listDesc = []
bigmlDesc = ''
string = ''
actualDesc = ''
cleanr = re.compile('<.*?>')
print(response)
for i in response.keys():
	if(i=='BigmlDesc_API_Response'):
		try:
			for j in response[i]['value']:
				listDesc.append(j['content'])
			bigmlDesc=' '.join(listDesc)
			bigmlDesc=re.sub(cleanr,'',bigmlDesc)
		except:
			pass
	if(i=='PageHTML'):
		try:
			string = response[i]
		except:
			pass
	if(i=='Diffbot'):
		try:
			diffBotDesc=response[i][0]["objects"][0]['text']
			diffBotDesc=re.sub(cleanr,'',diffBotDesc)
		except:
			pass


if(len(bigmlDesc)>len(diffBotDesc)):
	actualDesc=bigmlDesc
else:
	actualDesc=diffBotDesc

print(actualDesc)
