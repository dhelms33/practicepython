class Even:
    def __init__(self, lst):
        self.lst = lst
    def evens_only(self.lst):
        evens = []
        for element in self.lst:
            if element % 2 == 0:
                evens += element
        return evens
if __name__ == "__main__":
    try:
        user_input = int(input("Input a list to see the even elements in the list: "))
        obj_instance = Even(user_input)
        obj_instance.evens_only()
    except ValueError:
        print("Oh no! Please input a list!")