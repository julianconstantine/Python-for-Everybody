# Imports for both Python 2 and 3
import re

# Imports for Python 2
# import urllib
# from BeautifulSoup import *

# Imports for Python 3
import requests

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup

# Python 2
# url = raw_input("Enter URL: ")  # https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Carrich.html
# count = raw_input("Enter count: ")  # 7
# position = raw_input("Enter position: ")  # 18

# Python3
url = input("Enter URL: ")  # https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Carrich.html
count = input("Enter count: ")  # 7
position = input("Enter position: ")  # 18

# Re-cast as integers
count = int(count)
position = int(position)

for ii in range(count):
    # Python 2
    # html = urllib.urlopen(url).read()
    # html = requests.get(url).read()
    # soup = BeautifulSoup(html)

    # Python 3
    # Get HTML and parse via Beautiful Soup
    html = requests.get(url, verify=False)

    soup = BeautifulSoup(html.content, "lxml")
    tags = soup('a')

    jj = 1  # Counter
    for tag in tags:
        # Break once we go past the desired person (for the assignment, position = 18
        if jj > position:
            break

        # Get URL to page
        link_with_name = tag.get('href', None)

        # Extract name associated with URL
        if link_with_name is not None:
            name = re.findall(r'([A-Za-z]+).html$', link_with_name)
            name = name[0]

        jj += 1

    url = str(link_with_name)

    # Print link being "clicked" on by Python
    print("Following link " + url + " to " + name + "'s page.")

# Print desired result
print("\nThe name we are looking for is " + name + ".")
