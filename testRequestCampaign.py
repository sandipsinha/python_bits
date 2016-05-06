"""
" Author:       Sandip Sinha
" Email:        ssinha@loggly.com
"
"""

from mock import patch, Mock,MagicMock
import requests,json
from pythonmarketo.client import MarketoClient
import unittest


@patch.object(MarketoClient,'run_request_campaign')
   def test_marketo_request(self,mock_method):
      campaign_id=CONFIG.marketop.pcampaignID
      leadsid=[123456]
      mock_method.return_value=True
      values={'my.tshirtlink':'printfection.com/QwUl892'}
      mupd=mock_method(campaign_id,leadsid,values)
      self.assertTrue(mupd)
      assert mock_method.call_count,1
