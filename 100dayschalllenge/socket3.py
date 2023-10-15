import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('https://www.coursera.org/learn/python-network-data/lecture/MbRIS/12-3-unicode-characters-and-strings')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
    print(counts)
