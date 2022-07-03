import pickle

l = []
with open('iris.data','r') as f:
        read = f.readlines()
for lines in read:
        line = (lines.split('\n'))
        l.append(line)
        
with open('irs.pkl','wb') as f:
    pickle.dump(l,f)

file = 'irs.pkl'
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)

