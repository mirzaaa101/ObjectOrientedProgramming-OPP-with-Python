class MyCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc_sum(self):
        return self.num1 + self.num2

    def calc_div(self):
            try:
                return self.num1/self.num2
            except ZeroDivisionError:
                return f"Divisor cannot be zero"


my_clac_1  = MyCalculator(10,0)
print(my_clac_1.calc_div())

my_clac_1  = MyCalculator(10,5)
print(my_clac_1.calc_div())