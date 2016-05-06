def isPalindromic(x):
    xs = str(x)
    xsr = [letter for letter in xs]

    #print 'the new string is now', xsr
    #print 'the old string is now', ''.join(reversed(xsr))
    if xs == ''.join(reversed(xsr)):
        return True
    else:
        return False
        
        
x = 999

maxpalindrome = 999
while x > 1:
    y = 1        
    while y < 999:
         
        if maxpalindrome > x * y:
            pass
        else:
            if isPalindromic(x*y):
                maxpalindrome = x * y
        y += 1
    x -= 1
print 'the max palindrome number for %d*%d'%(x,y), 'is', maxpalindrome

