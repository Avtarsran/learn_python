def greater(num):
    if num > 5:
        return True
    else:
        return False

l = [12,32,2,3,33,2,4,33]
print(list(filter(greater,l)))