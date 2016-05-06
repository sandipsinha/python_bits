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
    query1 = ("select count(a.id), month(a.billdate) Months, year(a.billdate) Years from billing_table a where " \
              "a.billdate > (select min(billdate) from billing_table b where a.id = b.id) and " \
              "month(a.billdate) = %s and year(a.billdate) = %s group by month(a.billdate), year(a.billdate)")
    #print 'month', month, 'year', year
    cursor1 = cnx.cursor()
    cursor1.execute(query1,(month, year))
    activeCount = cursor1.fetchone()
    cursor1.close()
    if activeCount:
        return activeCount[0]
    else:
        return 0
    


def calc_monthly_churn(cnx):
    query2 = ("select count(final.id) eewholeft, sum(final.totalprofit) totalprofit,  month(final.finalmonth) finalmonth, year(final.finalmonth) finalyear from( " 
                "select id, max(date(billdate)) finalmonth, sum(amount) totalprofit   from billing_table group by id) final where year(final.finalmonth) = 2014 group by  "
                "month(final.finalmonth), year(final.finalmonth) order by year(final.finalmonth), month(final.finalmonth)")
    cursor = cnx.cursor()
    cursor.execute(query2)
    remaining_rows =  cursor.fetchall()
    totaleewholeft = 0
    totalltv = 0
    for items in remaining_rows:
        eewholeft, totalprofit, finalmonth, finalyear = items[0], items[1], items[2], items[3]
        
        currentKey = str(finalmonth) + '/' + str(finalyear)[2:4]   
        if eewholeft == 0:
            custChurn[currentKey] = 0
        else:
            getActiveCount = get_active_count(cnx, finalmonth, finalyear)
            if getActiveCount <= 0:
                print 'No Active employees'
                pass
            else:
                churnd =  round((float(eewholeft)/int(getActiveCount))*100,3)
                totaleewholeft += eewholeft
                totalltv += totalprofit
                #custChurn[currentKey] = churnd
    cursor.close()
    if totalltv > 0:
        return float(totalltv)/totaleewholeft 
    else:
        return 0

if __name__ == '__main__':
    get_connection = initDB(config)
    getclients = calc_monthly_churn(get_connection)
    print 'The LTV of average ACME user is {:6.2f}'.format(getclients)
 



        
