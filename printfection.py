"""
" Copyright:    Loggly, Inc.
" Author:       Sandip Sinha
" Email:        ssinha@loggly.com
" Last Updated: 04/07/2015
"
" Consumer routines for receiving and acting upon Frontend.Customer.Created and
" Registration.Customer.Cookie messages with respect to how they will be pushed
" into Marketo.
"
"""
import simplejson as json

from analytics_sync.consumers.utils   import make_logger
#from analytics_sync.consumers.config  import CONFIG
from analytics_sync.consumers.helpers import SubContextualizer, Gen2SubContextualizer
import urllib
import requests, json
from config import CONFIG
from pythonmarketo.client import MarketoClient

log = make_logger( 'mkto-account-consumers' )

client = Marketolient(host=CONFIG.marketo.rendpoint,client_id=CONFIG.marketo.clientid,client_secret=CONFIG.marketo.secret)


def get_update_prntfection_token():
    """
    For each new account created on the FrontEnd, it will created a new order in Printfection. Get the unique code and URL
    and update the account profile in Marketo.Marketo will then trigger off a email to the new account holder with the unique code and
     the unique URL.

    See this document: https://sites.google.com/a/loggly.com/loggly/Home/marketo-sfdc-migration
    """
    mklist=client.execute(method = 'get_leads_by_listId', listId = '676', fields=['email','firstName','lastName','company','postalCode'])

    #For logging
    logd = {
        'routing_key': 'Frontend.Customer.Created',
        'cursor': insert_and_convert_lead.consumer._cursor.get(),
        'endpoint': 'Marketo',
        'customer': {'subdomain':cust.get( 'subdomain' ), 'id':cust.get( 'id' )},
    }
    campaign_id=CONFIG.marketo.campid
    prntfecurl=CONFIG.marketo.prntfecurl
    data=json.dumps({'campaign_id':campaign_id})
    for s leads in mklist:
       r=requests.post(prntfecurl,data,auth=('f8d3962d6d5eb6d34caf65d31bdee6ad74e0d6b6',''))
       success = r.status_code != 200
       if success:
          logd.update( status = 'success' )
          log.info(logd )
       else:
           logd.update( status = 'failed', result = '%s' % r.status_code)
           log.crit(logd )


    
        email = leads.get('email')

        uniquecode=r['ucode'].parse('ascii')
        ulink=r['url'].parse('ascii') 


        #Doesn't matter.  Can't Map.
        res = client.execute(method = 'update_lead', lookupField = 'email', lookupValue = email, values = {'ucode':uniquecode, 'url':ulink})

        success = res.syncStatus.status != 'FAILED'

    if success:
        logd.update( status = 'success' )
        log.info(logd )
        success = res.leadId
    else:
        logd.update( status = 'failed', result = '%s' % res  )
        log.crit(logd )

    


    if '__main__' == __name__:
       get_update_prntfection_token()


