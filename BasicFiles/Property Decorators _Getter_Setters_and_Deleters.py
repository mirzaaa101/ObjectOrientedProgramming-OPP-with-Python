class Employee:
    def __init__(self,first='None', last='None',salary=0):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullName(self):
        return f"{self.first} {self.last}"

    @fullName.setter
    def set_fullname(self,new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    @email.getter
    def get_email(self):
        return self.email

    @email.deleter
    def dlt_email(self):
        self.first = None
        self.last = None

emp_1 = Employee('Mirza',"Abbas",50000)
emp_2 = Employee('Corey',"Shefer",60000)

del emp_1.dlt_email
print(emp_1.first)
print(emp_1.get_email)
print(emp_1.fullName)

