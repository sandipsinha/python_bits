from bs4 import BeautifulSoup
import urllib2
import re

lnk2follow = 'http://python-data.dr-chuck.net/known_by_Lisandro.html'
for count in xrange(7):
    response = urllib2.urlopen(lnk2follow)
    print response.info()
    html = BeautifulSoup(response.read(),"html.parser")
    linkn = 0
    name = ''
    for tag in html.find_all('li'):
        for hreflink in tag.find_all('a'):
            linkn += 1
            if linkn == 18:
                 lnk2follow = hreflink.attrs['href']
                 name = hreflink.contents
                 break
print ''.join(name)
                


