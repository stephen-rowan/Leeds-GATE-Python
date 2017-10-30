import json
import requests

json_file = '/home/stephen/Leeds-GATE/Code/Leeds-GATE-Python/items.json'

#json_file = requests.get('https://www.leedsgateheritage.com/api/tags')
#json_file = requests.get('https://www.leedsgateheritage.com/api/items')
#data = json.load(response)   
#print(data)

#data = json.loads(response.content)  
#print data

#print response.json
#rest_data = response

# convert the return into json data
#data = rest_data.json()  


with open(json_file) as json_data:

      data = json.load(json_data)
      #print(data)




for item in data[0].items():
    if item[0] == 'element_texts':
        #print item[0]
        #t = len(item[0])
        element_texts_range = len(item[1])
        print element_texts_range



for x in data:

    #print x['id']

    for i in range(element_texts_range):
        #print i
        print x['element_texts'][i]['element']['name'] + " : " + x['element_texts'][i]['text']
        
