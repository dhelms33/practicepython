class NumericFunctions:
    def __init__(self, num):
        self.num = num
    
    def fibonacci_gen(self):
        """ generates the nth fibonacci number"""
        if self.num <= 0:
            return 0
        elif self.num == 1:
            return 1
        fib_zero, fib_one = 0,1
        for num in range(2, self.num+1):
            fib_zero, fib_one = fib_zero, fib_zero + fib_one
        return fib_one
    
if __name__ == "__main__":
    try:
            user_input = int(input("Please enter a number to see the fibonacci sequence of that number: "))
            numeric_instance = NumericFunctions(user_input)
            result = numeric_instance.fibonacci_gen()
            print(f"The {user_input}th Fibonacci number is {result}")
    except ValueError:
            print("That is not an integer, try again")
            