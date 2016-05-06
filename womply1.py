import mysql.connector
import collections
custChurn = collections.OrderedDict()
config = {
  'user': 'root',
  'password': 'buktit02',
  'host': '127.0.0.1',
  'database': 'billing',
  'raise_on_warnings': True,
}
 

def initDB(*arg):
    return mysql.connector.connect(**config)



def get_active_count(cnx, month, year):
    query1 = ("select count(a.id), month(a.billdate) Months, year(a.billdate) Years from billing_table a where "
              "a.billdate > (select min(billdate) from billing_table b where a.id = b.id) and month(a.billdate) = %s "
              "and year(a.billdate) = %s group by month(a.billdate), year(a.billdate)")

    cursor1 = cnx.cursor()
    cursor1.execute(query1,(month, year))
    activeCount = cursor1.fetchone()
    cursor1.close()
    if activeCount:
        return activeCount[0]
    else:
        return 0
    


def calc_monthly_churn(cnx):
    query2 = ("select count(final.id) eewholeft, month(final.finalmonth) finalmonth, year(final.finalmonth) finalyear from( " 
                "select id, max(date(billdate)) finalmonth   from billing_table group by id) final  group by  "
                "month(final.finalmonth), year(final.finalmonth) order by year(final.finalmonth), month(final.finalmonth)")
    cursor = cnx.cursor()
    cursor.execute(query2)
    remaining_rows =  cursor.fetchall()
    for items in remaining_rows:
        eewholeft, finalmonth, finalyear = items[0], items[1], items[2]
        
        currentKey = str(finalmonth) + '/' + str(finalyear)[2:4]   
        if eewholeft == 0:
            custChurn[currentKey] = 0
        else:
            getActiveCount = get_active_count(cnx, finalmonth, finalyear)
            if getActiveCount <= 0:
                print 'No Active employees for {}-{}'.format(finalmonth, finalyear)
                pass
            else:
                churnd =  round((float(eewholeft)/int(getActiveCount))*100,3)
                custChurn[currentKey] = churnd
    cursor.close()
    if custChurn:
        return custChurn
    else:
        return None

if __name__ == '__main__':
    get_connection = initDB(config)
    getclients = calc_monthly_churn(get_connection)
    print getclients
 



        
