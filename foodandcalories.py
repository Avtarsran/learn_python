
n = input("Enter anythin: ")
lis = []
n = n.split(',')
# rev = n[:]
# rev.reverse()
# print(rev)
nr =n
for i in range(len(nr)//2):
    nr[len(nr) - i -1],nr[i] = nr[i],nr[len(nr) - i -1]
   
    print(nr[i])
    print(nr[len(nr)-i-1])
    
print(nr)