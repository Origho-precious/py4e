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

url = input('Enter the URL you want to scrape? ')
position = input('From the list returned which position do you want to crawl? ')
count = input('How many times do you want to run this program? ')

if len(url) < 1:
  url = 'http://py4e-data.dr-chuck.net/known_by_42.html'

if len(position) < 1:
  position = 3

if len(count) < 1:
  count = 4


print("Retrieving ", url)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
# print(soup.prettify())

def printNameInThirdTag(href, k):
  if(k >= 0):
    print("Retrieving ", href)
    newHtml = urlopen(href, context=ctx).read()
    soup = BeautifulSoup(newHtml, "html.parser")

    newTags = soup('a')
    
    # recursion
    printNameInThirdTag(newTags[int(position) - 1].get('href'), k - 1)
  else:
    return

printNameInThirdTag(tags[int(position) - 1].get('href'), int(count) - 1)
