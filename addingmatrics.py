m = int(input('enter the value of M: '))
n = int(input("Enter the value of N: "))

def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter {i} {j}\n"))
            row.append(inp)
        o.append(row)
    return o

a = matrix(m,n)
b = matrix(m,n)
print(a)
print(b)

def sum(a,b):
    output = []
    for i in range(len(a)):#no. of rows 
        row = []
        for j in range(len(a[0])):#no. of columns
            row.append(a[i][j]+b[i][j])
        output.append(row)
    return output

s = sum(a,b)
print(s)