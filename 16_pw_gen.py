import random

class Password:
    def __init__(self, first, second, last):
        self.first = first
        self.second = second
        self.last = last
        
    def gen_simple(self):
        dictionary = ["a", ",", "9", "*", "$", "#", "@", "@@#", ":", "{}[]"]
        password = ""
        for let in range(26):
            password += dictionary[random.randint]
        return password 
if __name__ == "__main__":
    try:
        user_input = input("Do you want a 26 character password? Enter Y or N")
        lower_ui = user_input.lower()
        if lower_ui == "No" or user_input == "N":
            
        obj_instance = Password()
            
    