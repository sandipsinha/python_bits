import urllib
import re
p = re.compile('\w+')

req = '*&%$#@~~*&T&*&h*&%%e%$#@i%$a%$t'
#r = p.findall(messystring)
r = p.findall(req)
print ''.join(r)
