def thousands_with_commas(i):
  si=str(i)[::-1]
  return (','.join(si[i:i+3] for i in range(0,len(si),3)))[::-1]
##    y=''
##    l=str(i)
##    m=l[::-1]
##    j=0
##    if len(l) > 3:
##        for letters in m:
##           if j%3 == 0 and j > 0: 
##              y+=',' + letters
##           else:
##              y+=letters
##           j+=1
##        print 'input', i , 'adn', y[::-1]
##        return y[::-1]
##    else:
##        print 'string', l
##        return l
        


if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
