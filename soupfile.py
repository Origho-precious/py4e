# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_1595915.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0

# Retrieve all of the anchor tags
tags = soup('span')
print("Count", len(tags))
for tag in tags:
  # Look at the parts of a tag
  total = total + int(tag.string)
print('Sum', total)