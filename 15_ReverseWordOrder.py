
class Reverse:
    def __init__(self, ls):
        self.ls = ls
    
    def reverse_order(self):
        words = self.ls.strip().split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
    
if __name__ == "__main__":
    try:
        user_input = input("Please input a string of multiple words")
        if not user_input or len(user_input.split()) < 2:
            raise ValueError("You must enter at least two words.")
        obj_instance = Reverse(user_input)
        result = obj_instance.reverse_order()
        print("Reversed word order: "result)
    except ValueError as ve:
        print(f"This is not a string, try again! {ve}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
            