class c2d:
    def __init__(self,icap,jcap):
        self.ic = icap
        self.jc = jcap
    def __str__(self):
        return f"{self.ic}i + {self.jc}j "

class c3d(c2d):
    def __init__(self,icap,jcap,kcap):
        super().__init__(icap , jcap)
        
        self.kc = kcap

    def __str__(self):
        return f"{self.ic}i + {self.jc}j + {self.kc}k "

g = c3d(2,3,45)
print(g)