import urllib
import json
import csv


#Retrieve api url :

#api_url = 'https://www.leedsgateheritage.com/api/tags'
api_url = 'https://www.leedsgateheritage.com/api/items'
#api_url = 'https://www.leedsgateheritage.com/api/collections'

#api_url = 'http://192.168.1.75/api/items'
#api_url = 'http://192.168.1.75/api/collections'


url = api_url
print 'Retrieving', url

open_url = urllib.urlopen(url)
data = open_url.read()
print 'Retrieved',len(data),'characters'


#csv file :

csv_out = open('api-items2.csv', mode='w') #opens csv file

writer = csv.writer(csv_out) #create the csv writer object


#Convert retrieved string into a json Python object :

data_python = json.loads(data)


#output = set([])

output = []
output2 = []

#for line in data_python:

#    for i in range(3):

#        print line["element_texts"][i]["element"]["name"], ":", line["element_texts"][i]["text"]

for D in data_python:

    if 'element_texts' in D:

        for d in D['element_texts']:

            k = d['element']['name']

            v = d['text']

            #print k, " : ", v

            #x = ("r", k)

            #writer.writerow((k, v))

 #           if v not in output2:
  #              output2.append(v)

            if k not in output:
                output.append(k)

writer.writerow(output)
#writer.writerow(output2)            




for D in data_python:

    if 'element_texts' in D:

        for d in D['element_texts']:
        
            k = d['element']['name']

            v = d['text']

            #print k, " : ", v

            #x = ("r", k)

            #writer.writerow((k, v))

            #for each in d:
            #    if each == 'text':
                    #print v
            #        output2.append(v)


            for line in d:
                if line == 'text':
                    print v
                #if each == 'text':
                 #   output2.append(v)


                    
        #print output2


        #writer.writerow(output2)
        #print k, v

#                print v
                #output2.append(v)
                #writer.writerow(output)
                #print output2





csv_out.close()

#print output

#print output2
