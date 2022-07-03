import os

def isbinod(file):
    with open(file,'r') as f:
        filecontent = f.read()
    if 'binod' in filecontent.lower():
        return True
    else:
        return False


dir_contents = os.listdir()
nbinod = 0
l = []
for item in dir_contents:
    if item.endswith('.txt'):
        flag = isbinod(item)

        if flag:
            nbinod += 1
            print(f"**binod found in {item}**")
            l.append(item)
            
            
        else:
            pass

print("binod detector summary")
print(f"{nbinod} files found with binod")
for items in l:
    print(items)