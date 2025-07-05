import BeautifulSoup
import requests 
class Decoder:
    def __init__(self, ins):
        self.ins = ins
        
    def how_to():
        help_me = print(help(requests))
        print(help_me)
    
    def decode_webpage(self.ins):
        url = 'http"//github.com'
        r = requests.get(url)
        r_html = r.text
        return r_html