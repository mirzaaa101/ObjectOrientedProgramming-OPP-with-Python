class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first='None', last='None',salary=0):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullName(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary *= self.raise_amount


emp_1 = Employee('Mirza',"Abbas",50000)
emp_2 = Employee('Corey',"Shefer",100000)
print(Employee.num_of_emps)

emp_1.raise_amount = 1.50
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.salary)
print(emp_2.salary)


