from mock import patch, Mock
from pythonmarketo.client import MarketoClient
from printfection2 import client
from config import CONFIG

@patch('pythonmarketo.client')
def test_marketo_read(self):
    mockclient=Mock(spec=client)
    mockclient.execute.return_value=[{'email':'ssinha@loggly.com','id':15343}]
    r= mockclient.execute(method = 'get_leads_by_listId', listId = CONFIG.marketo.listid, fields=['email','firstName','lastName','id'])
    self.assertTrue(mockclient.called)
    self.assertTrue(r==200)
    mockclient.execute.assert_called_once_with(fields=['email','firstName','lastName','id'],method = 'get_leads_by_listId', listId = CONFIG.marketo.listid)
    print r

test_marketo_read()
