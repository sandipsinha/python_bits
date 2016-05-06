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
#import simplejson as json

#from analytics_sync.consumers.utils   import make_logger
#from analytics_sync.consumers.config  import CONFIG
#from analytics_sync.consumers.helpers import SubContextualizer, Gen2SubContextualizer
import urllib
import requests, json
from config import CONFIG
from pythonmarketo.client import MarketoClient

#log = make_logger( 'mkto-campaign-printfection' )

client = MarketoClient(host=CONFIG.marketo.rendpoint,client_id=CONFIG.marketo.clientid,client_secret=CONFIG.marketo.secret)

def get_update_prntfection_token():
    """
    For each new account created on the FrontEnd, it will created a new order in Printfection. Get the unique code and URL
    and update the account profile in Marketo.Marketo will then trigger off a email to the new account holder with the unique code and
     the unique URL.

    See this document: https://sites.google.com/a/loggly.com/loggly/Home/marketo-sfdc-migration
    """

    try:
      #Get all the leads from Marketo that came in via this channel/Campaign   
       mklist=client.execute(method = 'get_leads_by_listId', listId = CONFIG.marketo.listid, fields=['email','firstName','lastName','id'])

       #For logging
       campaign_id=CONFIG.marketo.campaignID

       prntfecurl=CONFIG.marketo.prntfecurl
       data=json.dumps({'campaign_id':campaign_id})
#       data=json.dumps({'campaign_id':240374})
       #Loop thru the list and send the emails one by one        
       for leads in mklist:
            print leads['email']
            #First get the unique offer code and URL from Printfection for each new lead.
            r=requests.post(prntfecurl,data,auth=(CONFIG.marketo.prntfectionauth,''))
            success = r.status_code != 200
            #if success:
    ##            logd.update( status = 'success' )
    ##          log.info(logd )
    ##       else:
    ##           logd.update( status = 'failed', result = '%s' % r.status_code)
    ##           log.crit(logd )
    ##
            logd = {
                'customer': {'name': leads['firstName'] +' '+ leads['lastName'],'email':leads['email']} ,
                'endpoint': 'PrintFection'
                    }
    ##
    ##    
    ##        email = leads.get('email')
    ##
    ##        uniquecode=r['ucode'].parse('ascii')
    ##        ulink=r['url'].parse('ascii') 
    ##
    ##
    ##        #Doesn't matter.  Can't Map.
            leadid=[leads['id']]
            dataprnt=r.json()
            print 'The offer url', dataprnt['url'] , ' and lead id is', leads['id']
            #Next Update the leads profile with the temp offer code
            res = client.execute(method = 'update_lead', lookupField = 'id', lookupValue = leads['id'], values = {'tempOfferCode':dataprnt['url']})
            
            print 'The statue is', res
            
            res = client.execute(method = 'request_campaign', campaignID=campaign_id,leadsID=leadid,values={'my.tshirtlink':dataprnt['url']})

            print res

            #success = res.syncStatus.status != 'FAILED'

    ##    if success:
    ##        logd.update( status = 'success' )
    ##        log.info(logd )
    ##        success = res.leadId
    ##    else:
    ##        logd.update( status = 'failed', result = '%s' % res  )
    ##        log.crit(logd )
    except Exception as inst:
        print inst      # arguments stored in .args
##            print inst[0]['message']           # __str__ allows args to be printed directly
##            print inst[0]['code']           # __str__ allows args to be printed directly

    


if '__main__' == __name__:
   print 'About to call' 
   get_update_prntfection_token()

##except Exception as mesg:
##    print 'The exception is', mesg


