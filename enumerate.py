a = ('codewithharr','python.org','pythonlearning','therefore')

i = 0
for itme in a:
    i += 1
    if i%2==0:
        print(itme)
i1 = 0
for i,item in enumerate(a):
    if (i+1)%2==0:
        i1 += 1
        print(i1 , item)