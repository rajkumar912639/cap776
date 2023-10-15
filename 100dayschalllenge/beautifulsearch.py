
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter Location :')
html = urllib.request.urlopen(link).read().decode()
print("Retriving",link)
print('Received',len(html),'characters')

# Retrieve all of the anchor tags

sm=0
cn=0
data=ET.fromstring(html)
tags=data.findall('comments/comment')
for tag in tags:
    cn+=1
    sm +=int(tag.find('count').text)
print('count:', cn)
print('sum%d :',sm)