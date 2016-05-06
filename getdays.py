from datetime import datetime
import time
from datetime import timedelta
from collections import defaultdict


def mapdays(weekdays):
    weekdict = {0:'Monday',
                1:'Tuesday',
                2:'Wednesday',
                3:'Thursday',
                4:'Friday',
                5:'Saturday',
                6:'Sunday'
                }
    
    return weekdict[weekdays]

def getfreq(inptyear):
    maxdays = []
    yearday = defaultdict(int)
    yearday['Monday'] = 52
    yearday['Tuesday'] = 52
    yearday['Wednesday'] = 52
    yearday['Thursday'] = 52
    yearday['Friday'] = 52
    yearday['Saturday'] = 52
    yearday['Saturday'] = 52
    first_day_of_year = '01/01/'+ str(inptyear)
    current_date = datetime.strptime(first_day_of_year,'%m/%d/%Y')
    for x in xrange(365, 366):
        yearday[mapdays(current_date.weekday())] += 1
        current_date = current_date + timedelta(days=364)

    for key, value in yearday.iteritems():
        maxdays.append((value, key))
    maxsorted = sorted(maxdays, key=lambda x:x[0], reverse=True)

    kanoki= [x[1] for x in maxsorted]
    return maxsorted

print 'the maxmum number of days in the year 2016 is', getfreq(2860)
        
     


 
    
