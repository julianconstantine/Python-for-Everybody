import urllib
import json

serviceurl = 'https://www.google.com/maps/api/geocode/json?'

while True:
    address = raw_input("Enter location: ")
    if len(address) < 1:
        break

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
        continue

    print(json.dumps(jsdata, indent=4))

    lat = jsdata["results"][0]["geometry"]["location"]["lat"]
    lng = jsdata["results"][0]["geometry"]["location"]["lng"]

    print("Latitude: %f, Longitude: %f" % (lat, lng))

    # NOTE: Double vs. single quotes don't matter
    location = jsdata["results"][0]["formatted_address"]
    print(location)




