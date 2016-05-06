def subString(text2):
    a=0
    neww = ''
    for letter in text2:
        print 'the index is ' , text2.index(letter)
        neww = neww +   text2[0:text2.index(letter,a)]
        a += 1
    return neww+text2

test1 = 'abc'
print 'the explosion of letter is', subString(test1)
        
        
        
