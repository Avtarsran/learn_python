def searcher():
    import time
    book = 'This is a book written in kolkata by code with harry'
    time.sleep(4)
    
    while True:
        text = (yield) # acting as couroutines

        if text in book:
            print("your text is in the book")

        else:
            print('Your text is not in the in book')

# search = searcher()
# next(search)
# search.send("harry")
# input('press any key')
# search.send('code with harry')
# input('press any key')
# search.send('code')
# input('press any key')
# search.send('joker')
# search.close() # it will close the search and even if we call this function after this it will give an error
# search.send('joker')

def search():
    import time
    with open('name.txt','r') as f:
        read = f.read()
    time.sleep(3)
    
    while True:
        name = (yield)
        if name in read:
            print('your name is present')
        else:
            print('your name is not present')

ser = search()
next(ser)
ser.send('harry')
ser.send('bhavya')
ser.send('sirat')
ser.send('arsh')
ser.close()
ser.send('avtar')