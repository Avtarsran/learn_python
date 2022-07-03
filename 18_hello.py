class num:
    def __init__(self, r , i):
        self.i = i
        self.r = r
    def __add__(self, c ):
        return num(self.r + c.r , self.i + c.i)

    def __mul__(self, c ):
        mulreal = self.r*c.r - self.i * c.i
        mulimg = self.r * c.i + self.i * c.r
        return num(mulreal , mulimg)

    def __str__(self):
        return f"{self.r} - {self.i}i"

n1 = num(3 , 2)
n2 = num(1 , 7)
print(n1 + n2)
print(n1 * n2)