import time
from functools import lru_cache

@lru_cache(maxsize=int(input('enter the no. of calls= ')))


def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n
a = int(input('enter your number: '))

print('Now runing some work')
some_work(a)
some_work(a)
print("done")
some_work(a)
print('TERa YAAR POLICE EE AA')
some_work(a)
print('Called again')
some_work(a)
print('i will become pro in python by next three months')