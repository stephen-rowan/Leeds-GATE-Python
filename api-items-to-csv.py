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

fields = ['GATE Reference code','GATE Title','GATE Name of Creator','GATE Dates of Creation', 'GATE Level of description', 'GATE Collection', 'GATE Extent and medium of the unit of description', 'GATE Physical characteristics and technical requirements', 'GATE Conditions governing access'] 

#writes fields

writer.writerow(fields)



#loop through json data :


for line in data_python:
        

    for i in range(len(data_python)):
  
        print line["element_texts"][i]["element"]["name"], ":", line["element_texts"][i]["text"]


        if (line["element_texts"][i]["element"]["name"]).endswith('code'):
                    GATE_Reference_Code = (line["element_texts"][i]["text"])
        #else: GATE_Reference_Code = 0
        
        if (line["element_texts"][i]["element"]["name"]).endswith('Title'):
                    GATE_Title = (line["element_texts"][i]["text"])
        #else: GATE_Title = 0
                    
        if (line["element_texts"][i]["element"]["name"]).endswith('Creator'):
                   GATE_Name_of_Creator = (line["element_texts"][i]["text"])
        #else: GATE_Name_of_Creator = 0
        
        if (line["element_texts"][i]["element"]["name"]).endswith('Creation'):
                   GATE_Dates_of_Creation = (line["element_texts"][i]["text"])
        #else: GATE_Dates_of_Creation = 0
                   
        if (line["element_texts"][i]["element"]["name"]).endswith('Level of description'):
                   GATE_Level_of_description = (line["element_texts"][i]["text"])
        #else: GATE_Level_of_description = 0

        GATE_Collection = (line["collection"]["id"])

        if (line["element_texts"][i]["element"]["name"]).endswith('unit of description'):
                   GATE_Extent_and_medium_of_the_unit_of_description = (line["element_texts"][i]["text"])
        #else: GATE_Extent_and_medium_of_the_unit_of_description = 0                   

        if (line["element_texts"][i]["element"]["name"]).endswith('requirements'):
                    GATE_Physical_characteristics_and_technical_requirements = (line["element_texts"][i]["text"])
        else: GATE_Physical_characteristics_and_technical_requirements = 0

        if (line["element_texts"][i]["element"]["name"]).endswith('access'):
                   GATE_Conditions_governing_access = (line["element_texts"][i]["text"])
        #else: GATE_Conditions_governing_access = 0



                 

    writer.writerow([GATE_Reference_Code, GATE_Title, GATE_Name_of_Creator, GATE_Dates_of_Creation, GATE_Level_of_description, GATE_Collection, GATE_Extent_and_medium_of_the_unit_of_description, GATE_Physical_characteristics_and_technical_requirements, GATE_Conditions_governing_access])

                   

csv_out.close()
