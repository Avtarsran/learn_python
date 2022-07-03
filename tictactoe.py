def printboard(xrate,orate):
    zero = 'X' if xrate[0] else('0' if orate[0] else 0)
    one = 'X' if xrate[1] else('0' if orate[1] else 1)
    two = 'X' if xrate[2] else('0' if orate[2] else 2)
    three = 'X' if xrate[3] else('0' if orate[3] else 3)
    four = 'X' if xrate[4] else('0' if orate[4] else 4)
    five = 'X' if xrate[5] else('0' if orate[5] else 5)
    six = 'X' if xrate[6] else('0' if orate[6] else 6)
    seven = 'X' if xrate[7] else('0' if orate[7] else 7)
    eight = 'X' if xrate[8] else('0' if orate[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"__|___|___")
    print(f"{three} | {four} | {five}")
    print(f"__|___|___")
    print(f"{six} | {seven} | {eight}")
   

def sum(a,b,c):
    return a+b+c


def checkwin(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
            print("X Won the match")
            return 1
        
        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3):
            print("0 Won the match")
            return 0

    return -1


if __name__=="__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    ostate = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print("**Please don't enter same value**")
    while(True):
        printboard(xstate,ostate)

        if (turn == 1):
            print("X's turn")
            value = int(input('Please enter a vlue: '))
            xstate[value]= 1
        
        else:
            print("0's turn")
            value = int(input('Please enter a vlue: '))
            ostate[value] = 1
        turn = 1 - turn

        if xstate[value] == ostate[value]:
            turn = 1 - turn
            print('**please enter another value**')
            if turn==1:
                xstate[value]=0
            elif turn==0:
                ostate[value]=0

        cwin = checkwin(xstate,ostate)
        if (cwin != -1):
            print("Match Over")
            break

print(xstate,ostate)
