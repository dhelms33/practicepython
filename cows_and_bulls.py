import random
class SpecificGames:
    def __init__(self, ui):
        self.ui = ui
    def cows_and_bulls(self):
        count_cows = 0
        count_bulls = 0
        counter = 0
        choices = ["frog", "toad", "supercell", "snaul", "demo"]
        answer = random.
        for let in range(len(self.ui)):
            if let in self.ui[counter] == choices[counter]:
                count_cows +=1
            else:
                count_bulls +=1
            counter+=1
        return count_cows and count_bulls
            