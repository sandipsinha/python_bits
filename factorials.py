from array import array

def iseven(x):
  if x.isdigit():
    return int(x)+9 if int(x)%2==0 else int(x)

def sortest(inptstring):
   # testarray = sorted(inptstring, key=isascii)
    testarray = sorted(inptstring, key=lambda x:(x.islower(),x.isupper(),iseven(x)))
    return testarray

inptstr = 'HackerRank'

outputstring = array('B', map(ord,sortest(inptstr))).tostring()
print 'the output of sorted is',outputstring 
 
        
    
