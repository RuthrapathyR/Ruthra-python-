TTT=[]

def Initialize_Board():
    TTT.clear()
    for i in range(9):
        TTT.append('-')
    # OR
    #global TTT
    #TTT = ['-','-','-','-','-','-','-','-','-']

def Display_Board():
    print ("\t\tTic-Tac-Toe game")
    for i in range(9):
        print(TTT[i], '[', i+1, '] \t', end='')
        if (i+1)%3 == 0:
            print("\n")

def Move():
    for i in range(9):
        while True:
            if i%2 == 0:
                pos = int(input("Player 1 enter a position: "))
            else:
                pos = int(input("Player 2 enter a position: "))
            if pos >= 1 and pos <=9:
                if TTT[pos-1] != '-':
                    print("Please select only empty positions")
                else:
                    break
            else:
                print("Enter a valid position between 1 thru 9")
        if i%2 == 0:
            TTT[pos-1] = "X"
            Display_Board()
            if Check_Winner() == 1:
                print("Player 1 won!")
                break
        else:
            TTT[pos-1] = "O"
            Display_Board()
            if Check_Winner() == 1:
                print("Player 2 won!")
                break
    else:
        print("Match draw")

def Check_Winner():
    if TTT[0] == TTT[1] == TTT[2] == 'X':
        return 1
    if TTT[3] == TTT[4] == TTT[5] == 'X':
        return 1
    if TTT[6] == TTT[7] == TTT[8] == 'X':
        return 1
    if TTT[0] == TTT[3] == TTT[6] == 'X':
        return 1
    if TTT[1] == TTT[4] == TTT[7] == 'X':
        return 1
    if TTT[2] == TTT[5] == TTT[8] == 'X':
        return 1
    if TTT[0] == TTT[4] == TTT[8] == 'X':
        return 1
    if TTT[2] == TTT[4] == TTT[6] == 'X':
        return 1

    if TTT[0] == TTT[1] == TTT[2] == 'O':
        return 1
    if TTT[3] == TTT[4] == TTT[5] == 'O':
        return 1
    if TTT[6] == TTT[7] == TTT[8] == 'O':
        return 1
    if TTT[0] == TTT[3] == TTT[6] == 'O':
        return 1
    if TTT[1] == TTT[4] == TTT[7] == 'O':
        return 1
    if TTT[2] == TTT[5] == TTT[8] == 'O':
        return 1
    if TTT[0] == TTT[4] == TTT[8] == 'O':
        return 1
    if TTT[2] == TTT[4] == TTT[6] == 'O':
        return 1
    
    return 0

#__man__ starts
while True:
    Initialize_Board()
    Display_Board()
    Move()
    inp = input("Do you want to play again? (y/n)")
    if inp not in ('Y', 'y'):
        break
