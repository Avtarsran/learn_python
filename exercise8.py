import os

def soldier(path , format,file):
    os.chdir(path)
    i = 0
    p = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split('\n')
    for files in p:
        
        if files.endswith(format):
            i = i+1
            os.rename(files,f"{i}{format}")
        if files.endswith('.txt'):
            os.rename(files,files.capitalize())
       
    
    

    

soldier(r"D:\exercise8",".png",r"D:\exercise8\av.txt")
