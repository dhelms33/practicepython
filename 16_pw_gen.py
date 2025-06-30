import random

class Password:
    def __init__(self, first, second, last):
        self.first = first
        self.second = second
        self.third = third
        
    def gen_simple(self):
        dictionary = ["a", ",", "9", "*", "$", "#", "@", "@@#", ":", "{}[]"]
        password = ""
        for let in range(26):
            password += dictionary[random.randint]
    