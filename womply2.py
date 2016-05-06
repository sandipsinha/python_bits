import mysql.connector
import collections
    
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

def calculate_monthly_churn(clientIDs, cnx):
    month = 2
    year = 2014
    clientArr = [str(items) for items in clientIDs]
    clientString = '(' + ','.join(clientArr) + ')'

    cursor = cnx.cursor() 
    query1 = ("select count(ID) Counts from (SELECT ID, max(billdate) LastDate from billing_table where ID in %s group by ID) ab where " \
             "month(LastDate) = %s and year(LastDate) = %s group by LastDate")
    query2 = ("select count(a.id), month(a.billdate) Months, year(a.billdate) Years from billing_table a where "
             "a.billdate > (select min(billdate) from billing_table b where a.id = b.id) and month(a.billdate) = %s "
              "and year(a.billdate) = %s group by month(a.billdate), year(a.billdate)")
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
            dateKey = str(month) + '-' + str(year)
            month += 1
            if month == 12:
                year += 1
                month = 1
            if clientswholeft is not None and clientswholeft  > 0:
                cursor.close()
                cursor = cnx.cursor()
                cursor.execute(query2,(month, year))
                if cursor:
                    clientswhowereactivex = cursor.fetchone()
                    if clientswhowereactivex:
                        clientswhowereactive = clientswhowereactivex[0]
                        if clientswhowereactive > 0:
                            churnd = round((float(clientswholeft)/clientswhowereactive)*100, 3)
                            churndict[dateKey ] = '{}%'.format(float(churnd))
                        else:
                            churndict[dateKey ] = 0
                    else:
                        churndict[dateKey ] = 0
            if year == 2016 and month == 4:
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

if __name__ == '__main__':
    get_connection = initDB(config)
    getclients = get_cohorts(get_connection)
    january_cohort_churn =   calculate_monthly_churn(getclients,get_connection)
    if january_cohort_churn:
        print january_cohort_churn
    else:
        print 'Nothing Found for January 2014'
    get_connection.close()
