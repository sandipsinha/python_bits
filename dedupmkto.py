from pythonmarketo.client import MarketoClient
from config import CONFIG


client = MarketoClient(host = CONFIG.marketo.rendpoint,
                       client_id = CONFIG.marketo.clientid,
                       client_secret=CONFIG.marketo.secret)

def get_dedupe_mkto_leads(email):

    try:
        #Get all the leads from Marketo that belowng to this email
        filtervaluearray=[email]
        mklist=client.execute(method = 'get_multiple_leads_by_filter_type',
                              filterType = 'email', filterValues = filtervaluearray,
                              fieldslist=['email','firstName',
                                          'lastName', 'id', 'updatedAt', 'username__c', 'leadSource'])
        newlist=sorted(mklist, key=lambda k: k['updatedAt'],reverse=True)
        looseld=[]
        onecount=0
        for items in newlist:
            
            #The leads which have non-blank username are the winning lead by default
            if items['Username__c']:
                winld =  items['id']
                onecount+=1
            else:
                looseld.append(items['id'])
        '''Skip all if there are more than 1 leads with non-blank username
         if there are no records with non-blank usernames, next check is their source.
         The one which have 'Website direct' should be the winning lead'''            
        if onecount > 1:
            looseld=[]
            return False
        elif onecount == 0:
            looseld=[]
            for items in newlist:
                if items['leadSource'] == 'Website Direct' | onecount == 0:
                    winld =  items['id']
                    onecount+=1
                else:
                    looseld.append(items['id'])
                    
            #if nothing else works then pick the one which was updated the last
                    
            if onecount == 0:
                for items in newlist:
                    if onecount == 0:
                        winld =  items['id']
                        onecount+=1
                    else:
                        looseld.append(items['id'])
            
        #Finally if there is a winning lead and a list of valid loosing leads, call the merge API to merge the leads.
        if onecount == 1 and len(looseld) > 0:                    
            mklist=client.execute(method = 'merge_leads',
                                  winning_ld = winld,
                                  loosing_leads_list = looseld)
            return mklist
                
                
                
        print mklist

        print winld

        print looseld
        
    except Exception as inst:
            print inst      # arguments stored in .args

if '__main__' == __name__:
   print 'About to call', CONFIG.marketo.listid
   leadslist = client.execute(method = 'get_leads_by_listId',
                             listId = str(CONFIG.marketo.listid),
                             fields=['email'] ) 
   print 'length of items before', len(leadslist)
   leadset = set([d['email'] for d in leadslist])
   leadslist = list(leadset)
   print 'length of items after', len(leadslist)
   processedItems=[]
##   for lead in leadslist:
##       if lead['email'] in processedItems:
##           pass
##       else:
##           if get_dedupe_mkto_leads(lead['email']):
##               print 'lead successfully merged', lead['email']
##           else:
##               print 'lead not merged', lead['email']
##           processedItems.append(lead['email'])
    

         
     
