import requests
from bs4 import BeautifulSoup

class extract_page():

    def __init__(self, name):
        self.url = 'http://www.nytimes.com'
        url_text = requests.get(self.url)
        plain_text = url_text.text
        self.soup_text = BeautifulSoup(plain_text, "html.parser")
    
    
