a = 54
def func1():
    global a
    a = 8
    print(a)

func1()
print(a)