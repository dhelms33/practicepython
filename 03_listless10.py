class lists:
    @staticmethod
    def list_less_than_10(lst):
        if not lst:
            return("Please enter a list with at least one item")
        lower_list = []
        for item in list:
            if isinstance(item, int): 
                if item < 10:
                    lower_list.append(item)
                else:
                    return("All items must be integers")
        return lower_list

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of integers separated by commas: ")
        lst = [int(x.strip()) for x in user_input.split(",")]
        new_list=Lists.list_less_than_10(lst)
        print(new_list)
    except ValueError:
        print("Invalid input! Please enter only integers separated by commas!")