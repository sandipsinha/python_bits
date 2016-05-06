from string import maketrans
def findmainstring(str):
##    letter_count=dict(zip(string.ascii_lowercase,range(1,27)))
##    sentence =''
##    #print 'I am here', letter_count
##    for letter in str:
##        if letter.isalpha():
##            #print 'The letter is', len(letter.strip())
##            if letter != 'z' and letter != 'y' and len(letter.strip()) > 0 :
##                letvalue = letter_count[letter]
##                letvalue += 2
##                sentence = sentence + letter_count.keys()[letter_count.values().index(letvalue)]
##            elif letter == 'z':
##                sentence = sentence + 'b'
##            elif letter == 'y':
##                sentence = sentence + 'a'
##            elif len(letter.strip()) == 0:
##                sentence = sentence +  ' '
##        else:
##            sentence = sentence + letter
##    print sentence
    intab = "abcdefghijklmnopqrstuvwxyz"
    outab = "cdefghijklmnopqrstuvwxyzab"
    trantab = maketrans(intab, outab)
    print str.translate(trantab)
    


if __name__== "__main__":
    atext= 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
    atext = 'map'
    findmainstring(atext)
    








