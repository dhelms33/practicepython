class Games:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        
    def rock_paper_scissors(self.u1, self.u2):
        winner = ""
        if self.u1 == "Rock" and self.u2 == "Paper":
            winner = "User 2"
        else:
            winner = "User 1"
        if self.u1 == "Paper" and self.u2 == "Scissors":
            winner = "User 2"
        else:
            winner = "User 1"
        if self.u1 == "Scissors" and self.u2 == "Rock":
            winner = "User 2"
        else:
            winner = "User 1"
        return winner 
if __name__ == "__main__":
    try:
        user1_selection = input("Please input your choice user 1")
        user2_selection = input("Please input your choice user 2: ")
        games_instance = Games(user1_selection,user2_selection)
        games_instance.rock_paper_scissors()
    except ValueError:
        print("That is not an accepted input. Please enter Rock, Paper, or Scissors")