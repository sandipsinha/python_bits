import urllib
import re
p = re.compile('\w+')

req = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
#print 'The page', req
data = req.read()
dataarr = data.split('-->')
datalen = len(dataarr)
messystring = dataarr[:-1]
#r = p.findall(messystring)
ksing =  messystring[1].replace('<!--','')
r = p.findall(ksing)
print ''.join(r)
