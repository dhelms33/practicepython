class ElementSearch:
    def __init__(self, ui):
        self.ui = ui
    def find_element(self):
        target = self.ui
        for item in range(len(self.ui)):
            if item == target:
                return(f"The element " + target + "was found!")
            else:
                return("Item not found!")
if __name__ == "__main__":
    try:
        user_input = input("Please input a list of ordered elements: ")
        obj_instance = ElementSearch(user_input)
        result = obj_instance.find_element()
        print(result)
    except ValueError:
        print("This was not an ordered list of elements. Please try again.")