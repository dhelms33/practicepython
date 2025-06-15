#import UniqueLists
class UniqueFunctions():
    def __init__(self, a):
        self.a = a
    
    def first_last(self.a):
        first_element = self.a[0]
        last_element = self.a[-1]
        return first_element + " " + last_element
    
if __name__ == "__main__":
    try:
        
        user_input = int(input("Please input a list of numbers to get the first and last numbers: ")) 
        instance_unique = UniqueFunctions
        instance_unique.first_last(user_input)
    except ValueError:
        print("This is not a list of numbers, please try again!Q")