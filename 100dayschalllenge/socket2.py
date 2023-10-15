import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('https://www.coursera.org/learn/python-network-data/lecture/MbRIS/12-3-unicode-characters-and-strings')
for line in fhand:
    print(line.decode().strip())
