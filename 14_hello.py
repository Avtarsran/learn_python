class number:
    def __init__(self,num):
        self.num = num

    def __add__(self , num2):
        print("let's add")
        return self.num + num2.num

    def __mul__(self,num3):
        print("let's multiply")
        return self.num * num3.num

    def __str__(self):
        return f"decimal number : {self.num}"
    
    def __len__(self):
        return len(str(self.num))


n = number(9)
n = number(33)
print(n)
print(len(n))