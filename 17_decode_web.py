from bs4 import BeautifulSoup
import requests 
class Decoder:
    def __init__(self, ins):
        self.ins = ins
        
    def how_to():
        help_me = print(help(requests))
        print(help_me)
    
    def decode_webpage_text(self.ins):
        url = 'http"//github.com'
        r = requests.get(url)
        if self.ins == 'html':
            return r
        r_html = r.text
        return r_html
    def decode_soup(r):
        soup_text = BeautifulSoup(r)
        soup_pretty = soup_text.prettify()
        return soup_pretty
    
    