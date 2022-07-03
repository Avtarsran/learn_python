def fun(*args):
    print(type(args))
    if len(args)==2:
        print('The name of the student is',args[0],'and age is',args[1])
    elif (len(args)==3):
        print('The name of the student is',args[0],'and age is',args[1],'and roll no. is ',args[2])
lis = ['harry',22]
fun(*lis)

def printmarks(**kwargs):
    print(type(kwargs))
    for key ,value in kwargs.items():
        print(key , value)


marklist = {"harry":100,"Rohan":90,"vani verma":99,"sanket":98}
printmarks(**marklist)

def master(normal,*args , **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key , value)

master ('normal guy',*lis,**marklist)