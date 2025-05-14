class Division:
    def __init__(self, user_input):
        self.user_input = user_input

    def divisors(self):
        divisor_list = []
        for i in range(1, self.user_input):  # Start from 1 to avoid dividing by zero
            if self.user_input % i == 0:
                divisor_list.append(i)
        return divisor_list

if __name__ == "__main__":
    try:
        num = int(input("Please input a number to see all possible divisors: "))
        division_obj = Division(num)
        result = division_obj.divisors()
        print(result)
    except ValueError:
        print("Invalid input! Please input an integer!")