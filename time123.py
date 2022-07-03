import time

initial = time.time()
for i in range(45):
    print('this is harry bhai')
    time.sleep(2)
print(f"for loop ran in {time.time() - initial} seconds")

k = 0
while (k < 45):
    k += 1
    print('this is harry bhai')
print(f"while loop ran in {time.time() - initial} seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)
