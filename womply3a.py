import mysql.connector
import collections
import datetime
import numpy as np
import matplotlib.pyplot as pl
    
churndict = collections.OrderedDict()

config = {
  'user': 'root',
  'password': 'buktit02',
  'host': '127.0.0.1',
  'database': 'billing',
  'raise_on_warnings': True,
}

year = 2014

def initDB(*arg):
    return mysql.connector.connect(**config)

def get_total_left(cnx, month, year):
    query3 = ("select count(final.id) eewholeft, month(final.finalmonth) finalmonth, year(final.finalmonth) finalyear from( " \
                "select id, max(date(billdate)) finalmonth   from billing_table group by id) final where year(final.finalmonth) = %s " \
                 "and month(final.finalmonth) = %s group by month(final.finalmonth), year(final.finalmonth) order by year(final.finalmonth), month(final.finalmonth)")
    cursor = cnx.cursor()
    cursor.execute(query3,(year, month))
    eewholeft = cursor.fetchone()
    cursor.close()
    return eewholeft[0] if eewholeft else 0
    

def calculate_monthly_churn(clientIDs, cnx):
    month = 2
    year = 2014
    clientArr = [str(items) for items in clientIDs]
    clientString = '(' + ','.join(clientArr) + ')'

    cursor = cnx.cursor() 
    query1 = ("select count(ID) Counts from (SELECT ID, max(billdate) LastDate from billing_table where ID in %s group by ID) ab where " \
             "month(LastDate) = %s and year(LastDate) = %s group by LastDate")
    query2 = ("select count(a.id), month(a.billdate) Months, year(a.billdate) Years from billing_table a " \
              "where a.billdate > (select min(billdate) from billing_table b where a.id = b.id) " \
              "and month(a.billdate) = %s and year(a.billdate) = %s group by month(a.billdate), year(a.billdate)")

    while True:
        query1a = query1%(clientString,month,year)
        cursor.execute(query1a)
        clientswholeft = None
        try:
            if cursor:
                clientswholeftx = cursor.fetchone()
                if clientswholeftx:
                    clientswholeft = clientswholeftx[0]
                #print 'found something', clientswholeft
            dateKey =  str(year)[2:4] + '/' + str(month)
            totaleewholeft = get_total_left(cnx, month, year)

            if clientswholeft is not None and clientswholeft  > 0:
                cursor.close()
                cursor = cnx.cursor()
                cursor.execute(query2,(month, year))
                if cursor:
                    clientswhowereactivex = cursor.fetchone()
                    if clientswhowereactivex:
                        clientswhowereactive = clientswhowereactivex[0]
                        if clientswhowereactive > 0:
                            cohort = round((float(clientswholeft)/clientswhowereactive)*100, 3)
                            overallchurnrate = round((float( totaleewholeft)/clientswhowereactive)*100, 3)
                            churndict[dateKey ] =  [cohort, overallchurnrate]
                        else:
                            churndict[dateKey ] = 0
                    else:
                        churndict[dateKey ] = 0
            month += 1
            if month == 12:
                year += 1
                month = 1
            if year == 2016 and month == 3:
                break

        except TypeError as e:
            pass

    cursor.close()

    return churndict


        


def get_cohorts(cnx):
    billcohort = []
    query = ("SELECT id ID, min(BillDate) SubDate FROM billing.billing_table where BillDate = '2014-01-01' group by id")
    cursor = cnx.cursor()
    cursor.execute(query)

    for (ID, SubDate) in cursor:
        billcohort.append(ID)

    cursor.close()
    return billcohort

def create_chart(get_array):
    xaxis_1 = []
    xaxis_2 = []
    keya = []
    for key, values in get_array.items():
        keya.append(key)
        xaxis_1.append(values[0])
        xaxis_2.append(values[1])

         
            
    
    n_groups = len(keya)
    index = np.arange(n_groups)
    bar_width = .35
    opacity = .8

    rects1 = pl.bar(index, xaxis_1, bar_width,alpha=opacity, color='b', label='Jan-14 Churn Rate')
    rects2 = pl.bar(index+bar_width, xaxis_2, bar_width,alpha=opacity, color='r', label='Overall Churn Rate')

    pl.xlabel('Date')
    pl.ylabel('Churn Rate')
    pl.title('Monthly Churn Rate of Jan14 Cohort VS Overall ')
    pl.xticks(index + bar_width, keya)
    pl.legend()
    pl.tight_layout()
    pl.show()

if __name__ == '__main__':
    get_connection = initDB(config)
    getclients = get_cohorts(get_connection)
    january_cohort_churn =   calculate_monthly_churn(getclients,get_connection)
    if january_cohort_churn:
        create_chart(january_cohort_churn)
    else:
        print 'Nothing Found for January 2014'
    get_connection.close()
