class Nums:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def max_of_three(self):
        max = 0
        subset = [a,b,c]
        if (a > b) and (a > c):
            max = a
        elif (b > a) and (b > c):
            max = b
        else:
            max = c
        return max
    
#testing function
if __name__ == "__main__":
    try:
        user_input = int(input("Please input three numbers: "))
        obj_instance= Nums(user_input, user_input, user_input)
        result = obj_instance.max_of_three()
        print(result)
    except ValueError:
        print("This is not a correct line of ints separated by commas, try again.")
        