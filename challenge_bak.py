from collections import Counter
import random

def removenum(high, freq, sometuple):
    kenapple = []
    no_mult = 0
    for items in sometuple:
        q, r = items
        if q != high and r != high:
            no_mult += 1
            kenapple.append((q,r))
##        if q == high and r != 0:
##            ektaset = (r,0)
##            if ektaset  not in kenapple:
##                kenapple.append(ektaset)
##        elif r == high and q != 0:
##            ektaset = (q,0)
##            if ektaset not in kenapple == 0:
##                kenapple.append(ektaset)

    if no_mult == 0:
        kenapple = [] 
    #print 'The length of modifeid is ', len(kenapple)        
    #print sometuple, 'the list is now', kenapple, 'and the item is ' , high
    
    return tuple(kenapple)
def makelist(sometuple):
    somearray = []
    for items in sometuple:
        a, b = items
        #print items, 'and', a ,'*', b
        somearray.append(a)
        somearray.append(b)
        #print 'array', somearray
    
    return Counter(somearray).most_common()

def break_rings(lem):
    r = 0
    kano = makelist(lem)
    list1, list2 = zip(*kano)
    list1 = list(list1)
    #print 'List1', list1
    #print 'List2', list2
    current_min = 0
    for i in xrange(1):
        list1 =  [6, 2, 5, 1, 4, 8, 9, 7, 3]
        r = 0
        print 'The list is ' , list1
        bak = lem
        
        while len(bak) > 0:
            kano = makelist(bak)
            print 'kano' ,kano
            high, freq = kano[0]
            bak = removenum(list1[r], freq, bak)
            r += 1
            #print 'reading index #', r
        if current_min > 0:    
            current_min = min(current_min, r)
        else:
            current_min = r
        print 'the number is now ' , current_min   
    return current_min

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    #assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    #assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    #assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5
    #assert break_rings(({8,7},{1,9},{2,7},{3,6},{1,7},{5,7},{3,4},{9,5},{9,6},{3,5},)) == 3
