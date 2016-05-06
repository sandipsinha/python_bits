def findwordfreq(w,l):
    print 'the word and leteter is', w, ' adn ', l, 'and', l.count(w)
    return l.count(w)

def WordAnalysis():
    f=open('filesz.txt','r')

    wordfactory={}
    i=1
    for line in f:
        sline=line.replace("\n", "").split(' ')

        bline={}
        wordsz={}
        for items in sline:
           #print 'reading this word before', items , wordfactory.get(items)
           if items != '': 
               if items in wordfactory :
                   wordsz=wordfactory[items]
                   #print 'reading this word now', items , wordsz['count']
                   wordsz['count']=wordsz['count']+1
                   #print 'after reading this word ', items , wordsz['count']
               else:
                   wordsz['count']=1
               wordsz['line']=i
               wordfactory[items]=wordsz
               wordsz={}
           #print 'wrdfactort is now ', wordfactor        
        i+=1
    print  wordfactory
                  
                


WordAnalysis()
