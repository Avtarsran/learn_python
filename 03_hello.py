import random
rand = random.randint(1,100)
print(rand)

guess = 0
while True:
    print('press q to quit')
    a = input('enter your number')
    if a == 'q':
        print('thanks for playing this game')
        break
        
    else:
        a = int(a)
        if a==rand:
            print('you guessed it right')
            break
        elif a>rand:
            print('please enter lower number')
        elif a<rand:
            print('please enter higher number')
    guess += 1

print(f'you guessed it right in {guess} times')

with open('high.txt') as f :
    high = int(f.read())

if (high>guess):
    with open('high.txt', 'w') as f:
        f.write(str(guess))