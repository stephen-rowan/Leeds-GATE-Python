import json
import requests

#json_file = '/home/stephen/Leeds-GATE/Code/Leeds-GATE-Python/items.json'

#json_file = requests.get('https://www.leedsgateheritage.com/api/tags')
json_file = requests.get('https://www.leedsgateheritage.com/api/items')

data = json.loads(json_file.content)  


for item in data[0].items():

      if item[0] == 'element_texts':
        #print item[0]
        #t = len(item[0])
        element_texts_range = len(item[1])
        #print item[0]
        #print element_texts_range

      elif item[0] == 'collection':
          collection_range = len(item[1])
          #print item[0]
          #print collection_range

      elif item[0] == 'files':
          files_range = len(item[1])
          #print item[0]
          #print files_range

      elif item[0] == 'tags':
          tags_range = len(item[1])
          #print item[0]
          #print tags_range

      elif item[0] == 'extended_resources':
          extended_resources_range = len(item[1])
          #print item[0]
          #print extended_resources_range

      elif item[0] == 'owner':
            owner_range = len(item[1])
            #print item[0]
            #print owner_range

      else:
          print item[0]


        

for x in data:

    #print x['id']

      for i in range(element_texts_range):
        #print i
            print x['element_texts'][i]['element']['name'] + " : " + x['element_texts'][i]['text']
        
