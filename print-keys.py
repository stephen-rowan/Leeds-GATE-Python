import urllib
import json


#Retrieve api url :

api_url = 'https://www.leedsgateheritage.com/api/tags'
#api_url = 'https://www.leedsgateheritage.com/api/items'

url = api_url
print 'Retrieving', url

open_url = urllib.urlopen(url)
data = open_url.read()
print 'Retrieved',len(data),'characters'

#Convert retrieved string into a json Python object :

data_python = json.loads(data)

#data_python = json.load(data) 




#for key in data_python[0].keys():
#    print key


#for item in data_python[0].items():
#    print item

    
for value in data_python[0].values():
    print value
