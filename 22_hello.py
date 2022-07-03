lista = [13,44,44,44,44,23,24]
# b = []
# for items in lista:
#     if items%2==0:
#         b.append(items)
# print(b)
b = [i for i in lista if i%2==0]
print(b)

a = int(input('enter your starting number: '))
c = int(input('enter the ending number: '))
for i in range(a,c+1):
    flag = 0
    
    for j in range (2 , i):
        if i %j == 0:
            flag = 1

    if flag == 0:
        print(i)