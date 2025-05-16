from flask.cli import F


class SpecialLists:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b
    
    def common_list(self.list_a, self.list_b):
        max_length = 0
        common = []
        if len(self.list_a) > len(self.list_b):
            max_length = len(self.list_a)
        else:
            max_length = len(self.list_b)
        for item in range(max_length):
            if item in self.list_a and item in self.list_b:
                common.append(item)
        return common
    
    if __name__ == "__main__":
        try:
            user_input_list1 = input("Please enter list a: ")
            user_input_list2 = input("Please enter list b: ")
            result = SpecialLists(user_input_list1,user_input_list2)
            result.common_list
            #print(result) don't think I need this line
        except ValueError:
            print("Invalid input! Please input a list!")