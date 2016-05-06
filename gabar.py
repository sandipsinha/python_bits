import datetime
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as pl
import collections

def read_ingest():
    with open("log04.txt", 'r') as f:
        m = f.readline()
        loga = []
        logc = {}
        logf = defaultdict(dict)
        loge = defaultdict(int)
        logd = []
        indx = 0
        while m:
            logb = []
            loga = m.split()
            loge = defaultdict(str)
            tempd = loga[3].strip('[').strip(']')
            logdate = datetime.datetime.strptime(tempd,'%d/%b/%Y:%H:%M:%S')
            #print 'Date', logdate
            #print 'Index ', loga[8], type(loga[8])
            if loga[8] in logf[logdate.strftime('%Y/%m/%d')] > 0:
                logf[logdate.strftime('%Y/%m/%d')][loga[8]] += 1
            else:
                loge[loga[8]] = 1
                logf[logdate.strftime('%Y/%m/%d')][loga[8]] = 1
            #print loge
            #print logf
            m = f.readline()
        print logf
    return logf

def create_chart(get_array):
    xaxis_4 = []
    xaxis_2 = []
    xaxis_5 = []
    keya = []
    for key, values in get_array.items():
        keya.append(key)
        ind = ''

        for keyv, items in values.items():
            if keyv == '200':
                xaxis_2.append(items)
                ind = ind + '2'
            elif keyv == '400':
                ind = ind + '4'                
                xaxis_4.append(items)
            else:
                ind = ind + '5'
                xaxis_5.append(items)
        
        if ind == '235':
            pass
        elif ind == '24':
            #print 'now appending 0 to the 5th array'
            xaxis_5.append(0)
        elif ind == '25':
            xaxis_4.append(0)
        elif ind == '45':
            xaxis_2.append(0)
            
    
    n_groups = len(keya)
    index = np.arange(n_groups)
    bar_width = .35
    opacity = .8

    rects1 = pl.bar(index, xaxis_2, bar_width,alpha=opacity, color='b', label='200 - Success')
    rects2 = pl.bar(index+bar_width, xaxis_4, bar_width,alpha=opacity, color='r', label='400 - Not Found')
    rects3 = pl.bar(index+bar_width+bar_width, xaxis_5, bar_width,alpha=opacity, color='y', label='500 - Server Error')
    pl.xlabel('Date')
    pl.ylabel('Number of Errors / Day')
    pl.title('Error code tracking by date')
    pl.xticks(index + bar_width, keya)
    pl.legend()
    pl.tight_layout()
    pl.show()
             
    
            

get_array = read_ingest()
#print get_array
if get_array:
    sorteddict = collections.OrderedDict(sorted(get_array.items()))
    print sorteddict
    create_chart(sorteddict)
            
            
