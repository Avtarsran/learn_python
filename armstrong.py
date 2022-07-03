num = int(input('Enter the number you want to check: '))

sum = 0
order = len(str(num))
copy_n = num
while (num>0):
    digit = num%10
    sum += digit ** order
    num = num//10

if (sum == copy_n):
    print(f"{copy_n} is an armstrong number")
else:
    print(f"{copy_n} is not an armstrong number")