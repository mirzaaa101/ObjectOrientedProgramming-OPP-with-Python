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
        self.salary = int(self.salary*self.raise_amt)

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

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first='None', last='None',salary=0,prog_lang = "None"):
        super().__init__(first,last,salary)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first='None', last='None',salary=0,emps = None):
        super().__init__(first,last,salary)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps

    def add_emp(self,emp):
        if emp not in self.emps:
            self.emps.append(emp)
        else:
            print("This employee already exists")
    def rmv_emp(self,emp):
        if emp in self.emps:
            self.emps.remove(emp)
        else:
            print("This employee does not exist")

    def print_emps(self):
        for emp in self.emps:
            print(f"-->{emp.fullName()}")


dev_1 = Developer('Mirza',"Abbas",50000, "Python")
dev_2 = Developer('Corey',"Shefer",60000, "Java")

# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_1.fullName())
# print(dev_1.salary)
# dev_1.apply_raise()
# print(dev_1.salary)

# mng_1 = Manager("John","Doe",90000,[dev_1])
# print(mng_1.fullName())

# mng_1.add_emp(dev_2)
# mng_1.rmv_emp(dev_1)
# mng_1.print_emps()

# print(isinstance(dev_1,Developer))
# print(isinstance(dev_1,Employee))
# print(isinstance(dev_1,Manager))

print(issubclass(Developer,Employee))
print(issubclass(Employee,Developer))
print(issubclass(Manager,Employee))
print(issubclass(Developer,Manager))
