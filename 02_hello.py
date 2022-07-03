def greatest(n , n1 ,n2):
    if n>n1:
        g = n
    else:
        g = n1
    
    if g < n2:
        g = n2
    else:
        g
    return g

a = int(input('enter your number:'))
c = int(input('enter your number:'))
d = int(input('enter your number:'))
b = greatest(a,c,d)
print(b)