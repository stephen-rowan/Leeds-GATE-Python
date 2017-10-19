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

#field names

fields = ['GATE Reference code','GATE Title','GATE Name of Creator','GATE Dates of Creation'] 

#writes fields

writer.writerow(fields)

#loop through json data :


for line in data_python:
        

    for i in range(len(data_python)):
  
        print line["element_texts"][i]["element"]["name"], ":", line["element_texts"][i]["text"]


        if (line["element_texts"][i]["element"]["name"]).endswith('code'):
                    GATE_Reference_Code = (line["element_texts"][i]["text"])

        if (line["element_texts"][i]["element"]["name"]).endswith('Title'):
                    GATE_Title = (line["element_texts"][i]["text"])

        if (line["element_texts"][i]["element"]["name"]).endswith('Creator'):
                   GATE_Name_of_Creator = (line["element_texts"][i]["text"])

        if (line["element_texts"][i]["element"]["name"]).endswith('Creation'):
                   GATE_Dates_of_Creation = (line["element_texts"][i]["text"])


                   writer.writerow([GATE_Reference_Code, GATE_Title, GATE_Name_of_Creator, GATE_Dates_of_Creation])



csv_out.close()
