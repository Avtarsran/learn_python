class employee:
    company = 'bharat gas'
    salary = 5000
    bonus = 340

    @property
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary (self, val):
        self.bonus = val - self.salary 
   



e = employee()
print(e.totalsalary)
e.totalsalary = 69880
print(e.salary)
print(e.bonus)