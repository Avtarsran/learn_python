def game(you,comp):
    if comp==you:
        return None
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

player = input('press (g) for gun (W) for water (s) for snake')

import random
rand = random.randint(1,3)

if rand ==1:
    comp = 's'
elif rand==2:
    comp = 'w'
elif rand == 3:
    comp = 'g'
print(f"computer has chosen {comp} and Player has chosen {player}")

a = game(player,comp)
if a == None:
    print('its a tie')
elif a == True:
    print('player won')
elif a==False:
    print('computer won')