import os
old = 'log.txt'
new = 'logfile.txt'
with open (old) as f:
    r = f.read()
with open (new,'w') as f:
    f.write(r)

os.remove(old)