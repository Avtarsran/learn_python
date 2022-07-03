def fact(num):
    if num == 0 or num==1:
        return 1

    else:
        return num*fact(num-1)

def fac(number):
    i = 5
    count = 0
    while (number//i !=0):
        count += int(number/i)
        i = i*5
    return count


n = int(input('enter your number: '))


d = fac(n)
print(d)