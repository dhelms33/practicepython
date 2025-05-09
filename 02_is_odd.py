class nums:
    @staticmethod
    def odd_or_even():
        user_num = int(input("Please input a number to learn if it is even or odd"))
        answer = ""
        if user_num % 2 == 0:
            answer = "This number is even!"
        else:
            answer = "This number is odd!"
        return answer
if __name__ == "__main__":
    run_program = nums().odd_or_even()
    print(run_program)