def isPalindromic(x):
    xs = str(x)
    xsr = [letter for letter in xs]

    #print 'the new string is now', xsr
    #print 'the old string is now', ''.join(reversed(xsr))
    if xs == ''.join(reversed(xsr)):
        return True
    else:
        return False
        
    
print '906609 is palindromic', isPalindromic(906609)

##print '99999439 is  palindromic', isPalindromic(99999439)
##
##print '99999439 is  palindromic', isPalindromic(9999499)
##
##print '9995999 is  palindromic', isPalindromic(9995999)
        
