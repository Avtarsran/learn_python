class number:
    def sqare(self,num):
        self.num = num
        return num*num
    def cube(self,num):
        return num*num*num
    def squareroot(self,num):
        return num**0.5
    @staticmethod
    def greet():
        print('hello sir welocme to my blog')
n = int(input('enter your number: '))
g = number()
print(g.sqare(n))
print(g.squareroot(n))
print(g.cube(n))
g.greet()