import urllib
import json
import requests


#Retrieve api url :

#api_url = 'https://www.leedsgateheritage.com/api/tags'
api_url = 'https://www.leedsgateheritage.com/api/items'

#data = requests.get('https://www.leedsgateheritage.com/api/items')
#data = requests.get('https://www.leedsgateheritage.com/api/tags')

#print data.text

url = api_url
print 'Retrieving', url

open_url = urllib.urlopen(url)
data = open_url.read()
print 'Retrieved',len(data),'characters'

#Convert retrieved string into a json Python object :

data_python = json.loads(data)

print type (data)

#print data

#for key in data_python[0].keys():

 #   print key


for item in data_python[0].items():
    print item[0]

#element_texts 


#for value in data_python[0].values():
#    print value
    

#for k,v in data_python[1].items():
#    print k, ':', v


#iterates through range of json data :

#for i in range(len(data_python)):
#  
#    for key, value in data_python[i].items():
#
#        print key, value
#








