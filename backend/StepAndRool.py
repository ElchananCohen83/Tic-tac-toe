from computer import computer

############################################################

def check_step(tictactoe, bool, play, count):
    try:
        x, y = [int(i) for i in input().split()]
    except ValueError:
        print("Input is not a tow integer number.")
        return False
    if x < 0 or x > 3 or y < 0  or y > 3:
        print("This number out of array, plase give naumber between 1-3")
        return False
    if tictactoe[x-1][y-1] != '-':
        print("The location you selected is already taken, please choose another location")
        return False
    make_step(x, y,tictactoe, bool, play, count)

def make_step(x, y, tictactoe, bool, play, count):
    if play == '1':
        move(x, y, tictactoe, bool)
    else:
        tictactoe[x - 1][y - 1] = 'X' #ram mashich
        if count > 2:
            if win(tictactoe) == True:
                return
        computer(tictactoe, count)

############################################################

def move(x, y, tictactoe, bool):
    if bool == True:
        tictactoe[x - 1][y - 1] = 'O'
        print("Now X is playing")
    else:
        tictactoe[x - 1][y - 1] = 'X'
        print("Now O is playing")

############################################################

def win(tictactoe):
        for i in range(len(tictactoe)):
            if tictactoe[i][0] != '-' and tictactoe[i][0] == tictactoe[i][1] and tictactoe[i][2] == tictactoe[i][0]:#row
                print ('The game is over, the winner is ' + tictactoe[i][0])
                return True
        for i in range(len(tictactoe)):
            if tictactoe[0][i] != '-' and tictactoe[0][i] == tictactoe[1][i] and tictactoe[2][i] == tictactoe[0][i]: # column
                print('The game is over, the winner is ' + tictactoe[0][i])
                return True
        if tictactoe[0][0] != '-' and tictactoe[0][0] == tictactoe[1][1] and tictactoe[2][2] == tictactoe[0][0] or tictactoe[0][2] != '-' and tictactoe[0][2] == tictactoe[1][1] and tictactoe[2][0] == tictactoe[0][2]: # diagonally
            print('The game is over, the winner is ' + tictactoe[1][1])
            return True
        if '-' not in tictactoe[0] and '-' not in tictactoe[1] and '-' not in tictactoe[2]:
            print('המשחק הסתיים בתיקו')
            return True