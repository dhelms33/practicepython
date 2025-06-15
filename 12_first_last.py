#import UniqueLists
import ast
class UniqueFunctions():
    def __init__(self, a):
        self.a = a
    
    def first_last(self.a):
        first_element = self.a[0]
        last_element = self.a[-1]
        return str(first_element) + " " + str(last_element)
    
if __name__ == "__main__":
    try:
        
        user_input = int(input("Please input a list of numbers to get the first and last numbers: ")) 
        user_list = ast.literal_eval(user_input)
        if not isinstance(user_list, list):
            raise ValueError("Input is not a list.")
        
        instance_unique = UniqueFunctions(user_list)
        instance_unique.first_last()
    except ValueError:
        print("This is not a list of numbers, please try again!Q")