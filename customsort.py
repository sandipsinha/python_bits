import string, random
from multiprocessing import Process
from random import shuffle
import sys
import time
from multiprocessing import Pool


sortedkeystore = []
def genKeys():
    return ''.join(random.sample(string.ascii_lowercase, 26))

def extractsortkey(randomarray):
    inputarray = randomarray
    shuffle(randomarray)
    testarray = []
    sortedkey = None
    while not testarray == inputarray:
        sortedkey = genKeys()
        if sortedkey not in sortedkeystore:
            sortedkeystore.extend(sortedkey)
            #print 'The key is',  sortedkey, len(inputarray), len(randomarray)
            testarray = sorted(randomarray, key=lambda word: [sortedkey.index(c) for c in word])
            #print 'the length of the sorted array is', len(testarray)
    print 'The sorting key is', sortedkey
    return sortedkey
        



def getinputlist():
    with open('alphabet.txt') as f:
        readarray = [x.strip('\n').strip(' ') for x in f.readlines()]
        if readarray:
            return readarray
        else:
            print 'Array could not be read from the file'
            sys.exit(0)


def findsortedkey():
    getarray = getinputlist()
    t1 = time.time()
    print 'Got the array, now going to find the sorted key', len(getarray)
    getsortingKey = extractsortkey(getarray)
    if getsortingKey:
        print 'The sorting key is', getsortingKey
        t2 = time.time() - t1
        logging.info("Key extraction took  %0.2fs" % (t2))
    else:
        print 'Sorted key could not be extracted'
    return None
    
 

if __name__=='__main__':
    findsortedkey()
