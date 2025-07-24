from bs4 import BeautifulSoup
import requests 
import SpecificGames

class DecoderTwo(SpecificGames):
    def __init__(self, ui):
        self.ui = ui
        
    def print_to_screen(self):
        try:
            url = http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
            result_url = requests.get(url)
            webpage_content = ""
            if result_url == 200:
                webpage_content = result_url.text
            return webpage_content
                
        except ValueError as ve:
            print(f"An unknown error occurred while processing this webpage, " + {ve})
if __name__ == "__main__":
    user_input = input("Do you want to decode the monica-lewinsky webpage? Y or N")
    if user_input == ("Y"):
        obj_instance = DecoderTwo(user_input)
        result = obj_instance.print_to_screen()
        print(result)
    if user_input == ("N"):
        print("Oh well! I don't think it's anything to worry about!")
        
        
        
        