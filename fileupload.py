import requests

url = "http://192.168.1.13:5000/fileupld/"
files = {'filename': open('/Users/ssinha/Downloads/timsur.jpg', 'rb')}
r = requests.post(url, files=files)
