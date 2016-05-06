def getmeettimes(mettuple):
    getsorted = sorted(mettuple, key = lambda x:x[0])
    retlist = []
    secondmember = 0
    for index, members in enumerate(getsorted):
        firstmember = members[0]
        #print 'the index is', index
        if secondmember > firstmember:
            pass
        else:
            secondmember = members[1]
            for lookahead in getsorted[(index+1):]:
                #print 'seond member is' , members[1], lookahead
                if members[1] >= lookahead[0]:
                    secondmember = max(members[1],lookahead[1])
                    #print 'second member now is', secondmember 
            tuplemember =  (firstmember, secondmember)
            retlist.append(tuplemember)
            #print 'the retlist is now', retlist
    return retlist

x = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print 'the condensed meeting is', getmeettimes(x)
                                   
            
        
