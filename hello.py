import urllib.request, urllib.parse, urllib.error
import re

request = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1595915.html")

total = 0

for line in request:
  # print(line.decode().strip())
  lineWithNum = re.findall('^<tr>.+[0-9]+', line.decode().strip())
  if len(lineWithNum) < 1: continue
  # print(lineWithNum)
  for line in lineWithNum:
    value = re.findall('[0-9]+', line)
    for num in value:
      total = total + int(num)
    
print(total)