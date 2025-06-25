class Reverse:
    def __init__(self, ls):
        self.ls = ls
    
    def reverse_order(self.ls):
        reversed = ""
        for word in range(self.ls, -1):
            reversed = reversed + word
        return reversed
if __name__ == "__main__":
    try:
        user_input = input("Please input a string of multiple words")
        obj_instance = Reverse(user_input)
        result = obj_instance.reverse_order
        print(result)
    except ValueError:
        print("This is not a string, try again!")
            