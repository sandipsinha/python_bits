def getrepeatStrings(s):
    print 'the array to be debugged is', s
    arrayofchunks = []
    indx = 0
    lettersalreadylookedup = []
    while len(s) > indx + 1:
        print 'Now looking for', s[indx], s, indx
        if s[indx] in lettersalreadylookedup:
            k = lettersalreadylookedup[s.index(s[indx])-1:]
            k.append(s[indx])
            sdk = ''.join(k)
            arrayofchunks.append(sdk)
            print 'arrayofchunks is', arrayofchunks
            s = s[indx:] if indx  < len(s) else ''
            indx += 1
        else:
            lettersalreadylookedup.append(s[indx])
            indx += 1
        if not s:
            break
        elif indx == len(s):
            break
    return arrayofchunks

a='ttvmswxjzdgzqxotby_lslonwqaipchgqdo_yz_fqdagixyrobdjtnl_jqzpptzfcdcjjcpjjnnvopmh'       
print getrepeatStrings(a)
 

