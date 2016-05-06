from BeautifulSoup import BeautifulSoup
import urllib2
import re

response = urllib2.urlopen('http://python-data.dr-chuck.net/comments_217847.html')
print response.info()
html = BeautifulSoup(response.read())
tags = html('span')
sum = 0
for tag in tags:
    sum += int(tag.contents[0]) if re.match(r'\d*', tag.contents[0]) else 0
print sum


