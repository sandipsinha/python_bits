import datetime
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as pl

def read_ingest():
    with open("log03.txt", 'r') as f:
        m = f.readline()
        loga = []
        logc = defaultdict(list)
        logd = []
        while m:
            logb = []
            loga = m.split()
            tempd = loga[3].strip('[').strip(']')
            logdate = datetime.datetime.strptime(tempd,'%d/%b/%Y:%H:%M:%S')
            #print 'Already signed in', logc[loga[6].strip('/')]
            if logc[loga[6].strip('/')]:
                #print 't is not nnone', logc
                initial_array = logc[loga[6].strip('/')]
                initial_array.append((logdate,loga[8]))
                logc[loga[6].strip('/')]= initial_array
                #print 't is not nnone after', logc
            else:
                #print 't is none', len(logc)
                logc[loga[6].strip('/')]=[(logdate,loga[8])]   #[(logdate,loga[6].strip('/'),loga[8])]
            m = f.readline()
        print len(logc)
    return logc

def create_chart(get_array):
    fig = pl.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Error Codes')
    ax1.set_title('Analysis of Error codes')
    xaxis = []
    yaxis = []
    for key, values in get_array.items():
        keys = key
        for items in values:
            xaxis.append(items[0].date())
            yaxis.append(items[1])
    ax1.plot(xaxis, yaxis, 'ro')
    print yaxis.count('200')
    leg = ax1.legend()
    pl.show()
             
    
            

get_array = read_ingest()
if get_array:
    create_chart(get_array)
##if get_array:
##    create_chart(get_array)
            
