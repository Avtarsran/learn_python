class animals:
    pass
class pets(animals):
    pass
class dogs(pets):
    def bark(self):
        print('bhau bhau')

d = dogs()
d.bark()