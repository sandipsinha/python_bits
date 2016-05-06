from array import array
def isascii(chars):
    group = ''
    if str(chars).isalpha():
        #print 'the character is ', chars
        group = '1'
        if chars.islower():
            group = '11' + chars
        else:
            group = '12' + chars
        #print 'the group is', group
            
    else:
        print 'the character is', chars
        group = '2'
        if int(chars)%2==0:
            group = '22' + chars
        else:
            group = '21' + chars
    return group
        

def iseven(numbr):
    return numbr%2 == 0

def sortest(inptstring):
    testarray = sorted(inptstring, key=isascii)
    return testarray

inptstr = 'HackerRank'

outputstring = array('B', map(ord,sortest(inptstr))).tostring()
print 'the output of sorted is',outputstring 
 
        
    
