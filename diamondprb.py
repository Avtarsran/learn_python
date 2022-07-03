class a:
    def met(self):
        print('This is method fomr class a')
class b(a):
    def met(self):
        print('This is method fomr class B')
class c(a):
    def met(self):
        print('This is method fomr class C')
class d(c,a):
    def met(self):
        print('This is method fomr class D')
A = a()
B = b()
C = c()
D = d()

d.met("self")