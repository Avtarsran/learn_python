class number:
    def __init__(self,num):
        self.num = num

    def __add__(self , num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self,num3):
        print("let's multiply")
        return self.num * num3.num

n = number (4)
n1 = number (2)
sum = n + n1
print(sum)
mul = n * n1
print(mul)