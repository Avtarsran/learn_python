class person:
    country = 'india'
     
    def __init__(self):
        print('initializing \n person')

    def takebreath(self):
        print('i am breathing')
class employee(person):
    company = 'honda'

    def __init__(self):
        print('initializing \n employee')

    def takebreath(self):
        super().takebreath()
        print('i am luckily breathing')

class programmer(employee):
    company = 'fiverr'
    
    def __init__(self):
        super().__init__()
        print('initializing \n progammer')

    def getsalary (self):
        print(f"no salary to progammers")
    
    def takebreath(self):
        super().takebreath()
        print('i am a programmer so i am breathing')

p = person()
e = employee()
pr = programmer()

# p.takebreath()
# pr.takebreath()
# print(pr.company)
# print(pr.country)
