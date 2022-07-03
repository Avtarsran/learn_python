dic = {
    'pankha': 'fan',
    'dbba' : 'box',
    'diwar' : 'wall'
}

print(dic.keys())

a = input('enter the hindi word you want to translate: ')

# print('the value of the word is' , dic[a])

print('the value of above word is ', dic.get(a))