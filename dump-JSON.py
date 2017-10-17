import urllib
import json
import csv
#import ssl

#lgurl = 'https://www.leedsgateheritage.com/api/tags'
lgurl = 'https://www.leedsgateheritage.com/api/items'


url = lgurl
print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None

# Pretty print the JSON
print json.dumps(js, indent=4)

# Retrieve and print the Place ID
#placeID = js['results'][0]['place_id']
#print 'Place id: ', placeID




