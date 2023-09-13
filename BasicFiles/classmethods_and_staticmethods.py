class Employee:
    raise_amt = 1.04
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
        self.salary *= self.raise_amt

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def from_str(cls,emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first,last,salary)


    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# emp_1 = Employee('Mirza',"Abbas",50000)
# emp_2 = Employee('Corey',"Shefer",60000)

# Employee.set_raise_amt(1.05)
# emp_1.apply_raise()
# print(emp_1.salary)
# emp_2.apply_raise()
# print(emp_2.salary)

# emp_str_1 = 'Mirza-Abbas-50000'
# emp_str_2 = 'Corey-Shefer-60000'

# new_emp_1 = Employee.from_str(emp_str_1)
# new_emp_2 = Employee.from_str(emp_str_2)

# print(new_emp_1.email)
# print(new_emp_2.email)
# print(Employee.num_of_emps)

import datetime

my_day = datetime.date(2016,7,10)
print(Employee.is_working_day(my_day))


