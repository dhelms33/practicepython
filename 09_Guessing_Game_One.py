import Games
import random

class GuessingGame(Games):
    def guessing_game_one(user_int_input):
        random_number = random.randint(1,10)
        if user_int_input > random_number:
            return ("That is too high! Try again")
        elif user_int_input < random_number:
            return("That is too low! Try again")
        else:
            return("Correct!!")
        
if __name__ == "__main__":
    try:
        user_input = int(input("Please input a random number between 1 and 10"))
        guessing_game_instance = GuessingGame(user_input)
        guessing_game_instance.guessing_game_one()
    except ValueError:
        print("Please input an integer between 1 and 10!")