#! python 2.7

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

#address = raw_input("Enter location: ")
address = 'Oregon Institute of Technology'

url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
print("Retrieving " + str(url))

uh = urllib.urlopen(url)
data = uh.read()
print("Retrieved %i characters" % len(data))

try:
    jsdata = json.loads(str(data))
except: jsdata = None

if 'status' not in jsdata or jsdata['status'] != 'OK':
    print("=== Failure to Retrieve ===")
    print(data)

print(json.dumps(jsdata, indent=4))

# NOTE: Double vs. single quotes don't matter
place_id = str(jsdata['results'][0]['place_id'])
print(place_id)






