class programmer:
    company = 'micorosoft'
    def __init__ (self,name,product,work):
        self.name = name
        self.product = product
        self.work = work
    def getinfo(self):
        print(f"The name of empoloyee is {self.name}")
        print(f"The product name is {self.product}")
        print(f"The work he do is {self.work}")

g = programmer('harry','microsoft Excel','python coder')
g.getinfo()
print('-------------')
h = programmer('avtar','microsoft','stack overflower')
h.getinfo()