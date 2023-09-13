class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"

    def fullName(self):
        return f"{self.first} {self.last}"


# emp_1 = Employee('Mirza','Abbas',50000)
# emp_2 = Employee('A','B',30000)
# emp_2 = Employee('C','D',40000)
# emp_3 = Employee('E','F',60000)
# print(emp_1.fullName())
# print(emp_1.first)

emp_1 = Employee('Mirza','Abbas',50000)
print(emp_1.fullName())
print(Employee.fullName(emp_1))