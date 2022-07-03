class Employee:
    salary = 2000
    inc = 4
    
    @property
    def totalsalary(self):
        return self.salary * self.inc
    
    @totalsalary.setter
    def totalsalary(self , val):
        self.inc = val / self.salary

e = Employee()
e.totalsalary = 3000
print(e.salary)
print(e.inc)