n = int(input("Enter the numberse of apple harry got: "))
mn = int(input('Enter the mininmum range: '))
mx = int(input('Enter the maximum range: '))

for i in range(mn , mx+1):
    if mn==mx:
        print('this is not a range')
        print(f"{i} is diviser of {n}")

    else:
        if n%i==0:
            print(f"{i} is diviser of {n}")
        else:
            print(f"{i} is not a diviser of {n}")