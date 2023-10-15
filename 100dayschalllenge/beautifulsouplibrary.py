
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter - ')
html = urllib.request.urlopen(link, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
sm=0
cn=0
for tag in tags:
    cn+=1
    sm +=int(tag.contents[0])
print('count %d'% cn)
print('sum%d '% sm)