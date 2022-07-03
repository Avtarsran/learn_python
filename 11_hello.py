class employee:
    company = 'camel'
    salary = 100
    location = 'Delhi'
    
    @classmethod
    def changesalary(self,sal):
        self.salary = sal
        print(sal)

    

e = employee()
e.changesalary(232)
print(e.salary)
e.changesalary(108)