def prime(num):
    for i in range (2,num):
        if num%i==0:
            return False
        else:
            return True
l = [11,2,22,32,44,23,2]
print(list(filter(prime,l)))