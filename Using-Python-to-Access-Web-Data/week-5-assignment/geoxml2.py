#! python3

import requests
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_210562.xml'

r = requests.get(url)

# Using r.content gives problems
xml_tree = ET.fromstring(r.text)

# NOTE: Using xml_tree.findall('count') does NOT work, you have to use the .// in front
# The .// is something called an "XPath selector" which tells ET to find any tag named count
# I am not completely sure what just using 'count' does/why it only returns an empty string
count_tags = xml_tree.findall('.//count')
count_sum = 0

for i in range(len(count_tags)):
    count_sum += int(count_tags[i].text)

# count_sum comes out to 2,854
print(count_sum)
