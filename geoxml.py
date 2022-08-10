import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  total = 0
  url = input('Enter URL: ')
  if len(url) < 1: break

  print('Retrieving', url)
  uh = urllib.request.urlopen(url, context=ctx)

  data = uh.read()
  print('Retrieved', len(data), 'characters')
  tree = ET.fromstring(data)

  counts = tree.findall('.//count')
  
  for count in counts:
    if count.text is not None:
      total = total + int(count.text)
  
  print("Sum:", total)

# http://py4e-data.dr-chuck.net/comments_42.xml

# http://py4e-data.dr-chuck.net/comments_1595917.xml