class NoDups:
    def __init__(self, ls):
        self.ls = ls
    
    def no_dups(self):
        if len(self.ls) <= 1:
            return 1
        no_dups = []
        for item in range(len(self.ls)-1):
            if item in self.ls:
                pass
            else:
                no_dups += item
        return no_dups
if __name__ == "__main__":
    try:
        user_input = int(input("please enter a list of numbers to see the duplicates removed:"))
        no_dups_inst = NoDups(user_input)
        result = no_dups_inst.no_dups()
        print(result)
        
    except ValueError:
        print("This is not a integer or list of integers, please try again.")