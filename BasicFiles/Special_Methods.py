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

    def __str__(self):
        return f"Name:{self.fullName()}, Email:{self.email}"

    def __add__(self,other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.fullName())

emp_1 = Employee('Mirza',"Abbas",50000)
emp_2 = Employee('Corey',"Shefer",60000)

print(emp_1)

print(emp_1 + emp_2)
print(len(emp_1))