class VarStrings:
    def __init__(self, palindrome):
        self.palindrome = palindrome
    
    def is_palindrome(self.palindrome):
        if self.palindrome == list.reverse(self.palindrome):
            return True
        else:
            return False
if __name__ == "__main__":
    user_input = input("Please input a palindrome")
    obj_inst = VarStrings(user_input)
    try:
        obj_inst.is_palindrome
    except ValueError:
        print("Hey this isn't a string! Try again with a string!")