# Import urllib and BeautifulSoup modules
import urllib
from BeautifulSoup import *

# Link to web page with table
url = 'http://python-data.dr-chuck.net/comments_210565.html'

# Open URL and parse with BeautifulSoup
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Get all HTML span elements
spans = soup('span')

# Add up all numbers inside the spans
span_sum = 0

for span in spans:
    span_sum += int(span.contents[0])

# Print the result
print("The sum of all numbers in the table is %i" % span_sum)
