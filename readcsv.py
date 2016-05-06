import csv
import time
import datetime
import collections
import sys
with open('test.csv', 'rb') as csvf:
    spamreader = csv.reader(csvf, delimiter=',')
    presarray = []
    now = datetime.datetime.now()
    for row in spamreader:
        if row[0] == 'PRESIDENT':
            pass
        else:
            birthdate = time.strptime(row[1].strip(' '),'%b %d %Y')
            if row[3].strip(' '):
                expirydate = time.strptime(row[3].strip(' '),'%b %d %Y').tm_year
            else:
                expirydate = int(now.year)
            for x in xrange(birthdate.tm_year, expirydate,1):
                presarray.append((x,row[0]))
            
    sortedarray = [x[0] for x in presarray]
fructose=collections.Counter(sortedarray).most_common()
first_time = None
for items in fructose:
    if first_time:
        if first_time <> items[1]:
            sys.exit(1)
        else:
            print items[0]
    else:
        print items[0]
        first_time = items[1] 
