r = True
i = 1
with open ('log.txt','r') as f:
    while r:
        r = f.readline()


        if 'python' in r.lower():
            print('yes it is present')
            print(i)
            print(r)
        i = i+1