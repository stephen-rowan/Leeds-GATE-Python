import urllib
import json
import csv


#Retrieve api url :

api_url = 'https://www.leedsgateheritage.com/api/tags'
#lgurl = 'https://www.leedsgateheritage.com/api/items'

url = api_url
print 'Retrieving', url

open_url = urllib.urlopen(url)
data = open_url.read()
print 'Retrieved',len(data),'characters'

#Convert retrieved string into a json Python object :

data_python = json.loads(data) 


#csv file :

csv_out = open('api-tags.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['url','extended_resources','id','name'] #field names
writer.writerow(fields) #writes field



for line in data_python:
 
    #writes a row and gets the fields from the json object

    writer.writerow([line.get('url'),
                     line.get('extended_resources'),
                     line.get('id'),
                     line.get('name')])

csv_out.close()
    
