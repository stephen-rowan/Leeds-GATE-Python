import urllib
import json
import csv


#Retrieve api url :

collections_api_url = 'http://theafteraliceproject.org/api/collections'
items_api_url = 'http://theafteraliceproject.org/api/items'

collections_url = collections_api_url
items_url = items_api_url
print 'Retrieving', collections_url
print 'Retrieving', items_url


collections_open_url = urllib.urlopen(collections_url)
collections_data = collections_open_url.read()
print 'Retrieved',len(collections_data),'characters'


items_open_url = urllib.urlopen(items_url)
items_data = items_open_url.read()
print 'Retrieved',len(items_data),'characters'




#Convert retrieved string into a json Python object :


coll_data = json.loads(collections_data)
item_data = json.loads(items_data)

#y = d[3]["element_texts"][0]["text"]
#x = d[3]["element_texts"][1]["text"]
#print(d[0]["element_texts"][0]["text"])

for x in coll_data:
    y = x["element_texts"][0]["text"]
#    z = x["element_texts"][1]["text"]
    print(y)
#    print(z) 


for a in item_data:
    b = a["element_texts"][0]["text"]
#    z = x["element_texts"][1]["text"]
    print(b)




    

