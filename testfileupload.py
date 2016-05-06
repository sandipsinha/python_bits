import requests
from requests.auth import HTTPBasicAuth

print'running file upload'

url = 'https://storage.us2.oraclecloud.com'

with open('word.lst','rb') as payload:
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, auth=('amsandip@yahoo.com', 'Buktit02'),
                      data=payload, verify=False, headers=headers)
print 'The return code is', r

print 'Trying another way'

files = {'file': open('word.lst', 'rb')}

r = requests.post(url, auth=('amsandip@yahoo.com', 'Buktit02'), files=files)

print 'The result is', r.text

print'running file upload 3rd approach'

import json

payload = {'some': 'data'}

r = requests.post(url,auth=HTTPBasicAuth('amsandip@yahoo.com', 'Buktit02'), data=json.dumps(payload))

print 'The status code is', r.status_code
