class vec:
    def __init__(self , v):
        self.vec = v

    def __str__(self):
        str = ''
        i = 0
        for items in self.vec:
            str += f"{items}a{i} +"
            i = i+1
        return str[0:-1]
    def __add__(self,vec2):
        new = []
        for i in range (len(self.vec)):
            new.append(self.vec[i] + vec2.vec[i])
        return vec(new)
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]

        return sum

    def __len__(self):
        return len(self.vec)
v1 = vec([1,4])
v2 = vec([1,6.34,34])

if len(v1) == len(v2):

    print(v1 + v2)
    print(v1*v2)
    print(len(v1))
else:
    print("the lenght of both of the list is not same" )