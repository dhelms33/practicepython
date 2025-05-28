class Overlap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def lst_overlap(self):
        min_len = min(len(a), len(b))
        common = []
        for item in range(min_len):
            if item in a and item in b:
                common.append(item)
        return common
if __name__ == "__main__":
    try:
        user_input_a = input("Please input list 1 and wait")
        user_input_b = input("Please input list 2 to see the common elements")
        overlap_instance = Overlap(user_input_a, user_input_b)
        overlap_instance.lst_overlap()
    except ValueError:
        print("That is not a list! Try again")
        