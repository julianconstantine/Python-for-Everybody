#! python 3

import requests

# Need to use this URL: http://www.pythonlearn.com/code/intro-short.txt
# NOT this one: http://www.py4inf.com/code/intro_short.txt
# That's why my ETag and Last-Modified answers were wrong the first time

r = requests.get('http://www.pythonlearn.com/code/intro-short.txt')

for key in r.headers.keys():
    print(key + ": " + r.headers[key])

# Print out headers we want for the assignment
print("Last-Modified: " + r.headers['Last-Modified'])
print("ETag: " + r.headers['ETag'])
print("Content-Length: " + r.headers['Content-Length'])
print("Cache-Control: " + r.headers['Cache-Control'])
print("Content-Type: " + r.headers['Content-Type'])
