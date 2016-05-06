# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
wordin = []
worddict = {}
for x in xrange(n):
    wordin.append(raw_input())
    
for items in wordin:
    worddict[items] = worddict.get(items,0)  + 1

print len(worddict)
    
ab = [str(word) for word in worddict.values()]

print ' '.join(ab)

    

    
    


