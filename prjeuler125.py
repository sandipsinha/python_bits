def ispalindromic(num):
    sxa = str(num)
    if len(sxa) == 1:
        return True
    sxt = sxa[::-1]
    if sxa == sxt:
        return True
    else:
        return False
    

def find_seq(maxs,d,n):
    sx = 0
    keep_track = []
    palidromearray = []
    palindrome_so_far = 0
    while sx <= int(maxs):
        sx += n**2
        #print 'the sum total i snow', sx , 'and', maxs
        keep_track.append(n)
        if sx <= int(maxs):
            if ispalindromic(sx) and len(keep_track) > 1:
                palindrome_so_far = sx
                palidromearray.append(palindrome_so_far)
                #print 'The tag array is ', keep_track                    
                #print 'Array is now ', palidromearray, palindrome_so_far 
            else:
                pass
        
        n += d
    if palidromearray:
        keep_track.pop()
        print keep_track
        print 'the number is', palindrome_so_far
        return sum(palidromearray)
    else:
        return 0

def get_array(maxi,d):
    prec = []
    for number in xrange(1, maxi):
        xy = find_seq(maxi,d,number)
        if xy > 0:
            prec.append(xy)
    return prec

for items in xrange(input()):
    get_input = raw_input().split()
    maxn = int(get_input[0])
    diff = int(get_input[1])
    cx = get_array(maxn, diff)
    print 'The sum is ' , sum(cx)
    
        
        
