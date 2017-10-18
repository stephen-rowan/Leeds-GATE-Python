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


 
    #writes a row and gets the fields from the json object


#    print line["element_texts"][0]["element"]["name"], ":", line["element_texts"][0]["text"]

#    print line["element_texts"][1]["element"]["name"], ":", line["element_texts"][1]["text"]

for line in data_python:
        

    for i in range(len(data_python)):
  
        print line["element_texts"][i]["element"]["name"], ":", line["element_texts"][i]["text"]



        if (line["element_texts"][i]["element"]["name"]).endswith('code'):
                    GATE_Reference_Code = (line["element_texts"][i]["text"])


        if (line["element_texts"][i]["element"]["name"]).endswith('Title'):
                    GATE_Title = (line["element_texts"][i]["text"])
                    
                    writer.writerow([GATE_Reference_Code, GATE_Title])

                   



                    
#        GATE_Reference_Code = (line["element_texts"][0]["text"])
 #       GATE_Title = (line["element_texts"][0]["text"])
  #      GATE_Name_of_Creator = (line["element_texts"][0]["text"])
        



        

#    writer.writerow([line.get('id')])

       #writer.writerow([line.get(["element_texts"][0]["text"])])
    

#    writer.writerow(["element_texts"][0]["text"])

    #    writer.writerow([line.get('element_texts').get('element')])
    #writer.writerow([line.get('element_texts').get('GATE Reference code'),
     #                line.get('element_texts').get('GATE Title'),
      #               line.get('element_texts').get('GATE Name of Creator'),
       #              line.get('element_texts').get('GATE Dates of Creation')])



csv_out.close()
