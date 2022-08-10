import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  total = 0
  url = input('Enter Location: ')
  if len(url) < 1: break
  
  print('Retrieving', url)
  uh = urllib.request.urlopen(url, context=ctx)

  data = uh.read()
  # print(data.decode()) // Similar to json.loads(data)

  info = json.loads(data)
  print('Retrieved', len(info['comments']), 'characters')

  for item in info['comments']:
    total = total + int(item['count'])
    
  print(total)

# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1595918.json