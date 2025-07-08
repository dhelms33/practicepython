from bs4 import BeautifulSoup
import requests 
class Decoder:
    """
    A class to fetch and decode HTML content from a given webpage
    """
    def __init__(self, url):
        self.url = url
    
    def fetch_html(self) -> str:
        """fetches raw HTML from the URL"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        
    def how_to():
        help_me = print(help(requests))
        print(help_me)
    
    def decode_webpage_text(self.url):
        url = 'http"//github.com'
        r = requests.get(url)
        if self.url == 'html':
            return r
        r_html = r.text
        return r_html
    def decode_soup(r):
        soup_text = BeautifulSoup(r)
        soup_pretty = soup_text.prettify()
        return soup_pretty
    
if __name__ == "__main__":
    try:
        user_input = input("Please input 1 if you want your decrypted website in html or 2 if you want your decrypted website prettied using decode soup")
        obj_instance = Decoder(user_input)
        result = obj_instance.decode_webpage_text
    except ValueError:
        print("This is not one or two, please try again!")
    
    