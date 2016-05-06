from collections import defaultdict
##import collections
##def annograms(word):
##    print 'word', word
##    test1=sorted(list(word))
##    cwords=[w.rstrip() for w in open('WORD.LST')]
##    x=[]
##    wordl=list(word)
##    a=collections.Counter(wordl)
##    ab=a.most_common(1)
##
##    
##    words =[w for w in cwords if len(w) == len(word)]
##    #print 'Length of word array', len(words)
##    for items in words:
##        word2=list(items)
##        ac=collections.Counter(word2)
##        ad=ac.most_common(1)
##        
##        if ab==ad:
##            #print 'The chosen word is', items
##            if sorted(list(items))==test1:
##                #print 'it was actualy added', items
##                x.append(items)
    
##    return x

def annograms(word):
  words_by_anagram=defaultdict(set)
  for word in [w.rstrip() for w in open('WORD.LST')]:
    words_by_anagram[''.join(sorted(word))].add(word)
  return words_by_anagram[word]

        



if __name__ == "__main__":
    print 'started'
    print annograms("train")
    print '--'
    print annograms('drive')
    print '--'
    print annograms('python')
