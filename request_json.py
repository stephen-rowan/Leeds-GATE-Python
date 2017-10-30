import requests
import json


#response = requests.get('https://www.leedsgateheritage.com/api/tags')
response = requests.get('https://www.leedsgateheritage.com/api/items')
#data = json.load(response)   
#print(data)

#data = json.loads(response.content)  
#print data

#print response.json
rest_data = response

# convert the return into json data
data = rest_data.json()  

# parse the json data

for x in data:

    print x['id']

    #GATE Reference code
    #print x['element_texts'][0]['element']['name'] + " : " + x['element_texts'][0]['text']

    if 'GATE Reference code' in x['element_texts'][0]['element']['name']:
            print x['element_texts'][0]['element']['name'] + " : " + x['element_texts'][0]['text']
                
    #GATE Title
    #print x['element_texts'][1]['element']['name'] + " : " + x['element_texts'][1]['text']

    #GATE Name of Creator
    #print x['element_texts'][2]['element']['name'] + " : " + x['element_texts'][2]['text']

    #GATE Dates of Creation
    #print x['element_texts'][3]['element']['name'] + " : " + x['element_texts'][3]['text']

    ##GATE Level of description
    #print x['element_texts'][4]['element']['name'] + " : " + x['element_texts'][4]['text']
    #
    ##GATE Extent and medium of the unit of description
    #print x['element_texts'][5]['element']['name'] + " : " + x['element_texts'][5]['text']
    #
    ##GATE Conditions governing access
    #print x['element_texts'][6]['element']['name'] + " : " + x['element_texts'][6]['text']
    #
    ##GATE Conditions governing reproduction
    #print x['element_texts'][7]['element']['name'] + " : " + x['element_texts'][7]['text']
    #
    ##GATE Language of material
    #print x['element_texts'][8]['element']['name'] + " : " + x['element_texts'][8]['text']
    #
    ##GATE Description
    #print x['element_texts'][9]['element']['name'] + " : " + x['element_texts'][9]['text']
    #
    ##GATE Date(s) of description
    #print x['element_texts'][10]['element']['name'] + " : " + x['element_texts'][10]['text']
    #
    ##GATE Geographical area
    #print x['element_texts'][11]['element']['name'] + " : " + x['element_texts'][11]['text']
    #
    ##GATE Immediate source of acquisition or transfer
    #print x['element_texts'][12]['element']['name'] + " : " + x['element_texts'][12]['text']
    #
    #if 'GATE Current location' in x:
    #    print x['element_texts'][13]['element']['name'] + " : " + x['element_texts'][13]['text']
    #

    if 'GATE Related units of description' in x['element_texts'][14]['element']['name']:
            print x['element_texts'][14]['element']['name'] + " : " + x['element_texts'][14]['text']

    #
    #GATE Related units of description
    #print x['element_texts'][14]['element']['name'] + " : " + x['element_texts'][14]['text']









    


    

#for item in data[0].items():
#
#    for x in item:
#        if type (x) == list:
#
#            print type (x)
#            print x
#        #else:

         #   print type(x)
