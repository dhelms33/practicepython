class Primarlity:
    def __init__(self, isPrime):
        self.isPrime = isPrime 
    
    def Prime(self.isPrime):
        if self.isPrime % 2 != 0:
            return("This is prime!")
        else:
            return("This is not prime!")
if __name__ == "__main__":
    try:
        user_input = int(input("Please enter a number to see if it's prime."))
        obj_instance = Primarlity(user_input)
        obj_instance.isPrime
    except ValueError:
        print("This is not an accepted value, try again.")
        