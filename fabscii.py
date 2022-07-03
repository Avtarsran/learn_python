import time
def fabscii(num):
    if num==1 or num==0:
        return 1
    
    else:
        return (fabscii(num-1)+fabscii(num-2))


def fab(n):
    prev = 0
    current = 1
    for i in range(1,n):
        prevprev = prev
        prev = current
        current = prevprev + prev
    yield current


n = int(input('enter your number: '))
a = fab(n)

ier = iter(a)
print(next(ier))



init = time.time()
print(f"it took {time.time() - init} seconds")