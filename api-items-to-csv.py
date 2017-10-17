import urllib
import json
import csv


#Retrieve api url :

#api_url = 'https://www.leedsgateheritage.com/api/tags'
api_url = 'https://www.leedsgateheritage.com/api/items'

url = api_url
print 'Retrieving', url

open_url = urllib.urlopen(url)
data = open_url.read()
print 'Retrieved',len(data),'characters'

#Convert retrieved string into a json Python object :

data_python = json.loads(data) 


#csv file :

csv_out = open('api-items.csv', mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['GATE Reference code','GATE Title','GATE Name of Creator','GATE Dates of Creation'] #field names
writer.writerow(fields) #writes field

#loop through json data :

for line in data_python:
 
    #writes a row and gets the fields from the json object

    writer.writerow([line.get('id')])


#    writer.writerow([line.get('element_texts')])

    
#    writer.writerow([line.get('element_texts').get('element')])



    
    #writer.writerow([line.get('element_texts').get('GATE Reference code'),
     #                line.get('element_texts').get('GATE Title'),
      #               line.get('element_texts').get('GATE Name of Creator'),
       #              line.get('element_texts').get('GATE Dates of Creation')])
    

csv_out.close()
    

