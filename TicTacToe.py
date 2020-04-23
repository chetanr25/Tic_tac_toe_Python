def slow():
    for x in range(100000000):
        x = x +1

def delay(str):
    for x in len(str):
        print(str(x))
        slow()

def printco(Commands, chance):
    if chance != 0:
        for x in range(10):
            if Commands[x] != '':
                print( Commands[x])

def printbo(Board):
    for x in range(9):
        print( Board[x], end = "")

def check(Board, ch):
    bol = False
    for x in range(len(Board[ch-1])):
        if (Board[ch-1])[x] == '-':
            bol = True
            return bol
            break
    return bol

def replac (Board, letter, ch):
    Board[ch-1] = Board[ch-1].replace('-' , letter)
    return Board

def w(a,b,c,l):
    b1 = [False, False, False]
    b1[0] = l in a
    b1[1] = l in b
    b1[2] = l in c
    c2 = False
    if False in b1:
        c2 = False
    else:
        c2 = True
    return (c2)

def wins(board, l):
    bol = [False, False, False, False, False, False, False, False]
   # if board[0] == board[4]  == board[8] :
    #    bol[0] = True
    bol[0] = w(board[0], board[4], board[8],l)
    bol[1] = w(board[2], board[4], board[6],l)
    bol[2] = w(board[0], board[1], board[2],l)
    bol[3] = w(board[3], board[4], board[5],l)
    bol[4] = w(board[6], board[7], board[8],l)
    bol[5] = w(board[0], board[3], board[6],l)
    bol[6] = w(board[1], board[4], board[7],l)
    bol[7] = w(board[2], board[5], board[8],l)
    p = True in bol
    if p:
        return p
    else :
        return p

def swap(Player, Letter, Commands, Board , Chance):
    end = False
    while end == False:
        printbo(Board)
        printco(Commands, Chance)
        ch = int(input(Player + ' Enter your choice: '))
        if  ch < 1 and ch > 9:
            print('\fWrong input !')
            continue
        che = check(Board, ch )
        if che == False:
            print('\fAlready assigned')
            continue
        Board = replac(Board, Letter, ch)
        if wins(Board, Letter) == True :
            printbo(Board)
            print(Player + '  :   Wins !')            
            exit()
        c = 0
        for x in range(len(Board)):
            for x2 in range(len(Board[x])):
                if (Board[x])[x2] == '-':
                    c = c + 1
        if c == 0 :
            printbo(Board)
            print('\n')
            print('Draw. ha.ha.ha...')
            exit()
        end = True
        print('\f\f\f\f\f\f\f')
        break
Board = [" - | ", " - | " , " - | \n",
         " - | ", " - | " , " - | \n",
         " - | ", " - | " , " - | \n\n"]
GamesPlayed = 0
Player1 = input("enter name of player1")
Player2 = input("enter name of player2")
Play1_letter = "X"
Play2_letter = "O"
print(Player1 ,' using ', Play1_letter)
print(Player2 ,' using ', Play2_letter)
print('\nStarting the game')
Chance = 0
Commands = ['Commands:','','','','','','','','','']
while True:
    if GamesPlayed % 2 == 0:
        swap(Player1, Play1_letter, Commands, Board, Chance)
        swap(Player2, Play2_letter, Commands, Board, Chance)
    else :
        Play1_letter,Play2_letter = Play2_letter,Play1_letter
        swap(Player2, Play2_letter, Commands, Board, Chance)
        swap(Player1, Play1_letter, Commands, Board, Chance)
