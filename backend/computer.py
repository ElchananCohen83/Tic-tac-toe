############################################################
def computer(tictactoe, count):
    if count == 1:
        if tictactoe[1][1] == '-':
            tictactoe[1][1] = 'O'
            return
        else:
            tictactoe[0][0] = 'O'
            return

    if checkrow_O(tictactoe) == True:
        return
    if checkcolumn_O(tictactoe) == True:
        return
    if checkcdiagonally(tictactoe) == True:
        return
    if checkrow_X(tictactoe) == True:
        return
    if checkcolumn_X(tictactoe) == True:
        return
    if check3slots(tictactoe) == True:
        return

############################################################

def checkrow_O(tictactoe):
    for i in range(len(tictactoe)):
        if '-' in tictactoe[i]:
            for j in range(len(tictactoe[i])):
                if tictactoe[i].count('O') == 2:
                    if tictactoe[i][j] == '-':
                        tictactoe[i][j] = 'O'
                        return True

############################################################

def checkcolumn_O(tictactoe:list):
    for i in range(len(tictactoe)):
            if tictactoe[0][i] == 'O' and tictactoe[0][i] == tictactoe[1][i]:
                if tictactoe[2][i] == '-':
                    tictactoe[2][i] = 'O'
                    return True
            if tictactoe[1][i] == 'O' and tictactoe[1][i] == tictactoe[2][i]:
                if tictactoe[0][i] == '-':
                    tictactoe[0][i] = 'O'
                    return True
            if tictactoe[0][i] != '-' and tictactoe[0][i] == tictactoe[2][i]:
                if tictactoe[1][i] == '-':
                    tictactoe[1][i] = 'O'
                    return True

############################################################

def checkcdiagonally(tictactoe: list):
    #checkcdiagonally_from left to right
        if tictactoe[0][0] == tictactoe[1][1]: # if... == 'O'
            if tictactoe[2][2] == '-':
                tictactoe[2][2] = 'O'
                return True
        if tictactoe[1][1] != '-' and tictactoe[1][1] == tictactoe[2][2]:
            if tictactoe[0][0] == '-':
                tictactoe[0][0] = 'O'
                return True
            else:
                if tictactoe[0][2] == '-':
                    tictactoe[0][2] = 'O'
                    return True
                2
                if tictactoe[0][1] == '-':
                    tictactoe[0][1] = 'O'
                    return True

    #checkcdiagonally_from righ to tleft
        if tictactoe[0][2] != '-' and tictactoe[0][2] == tictactoe[1][1]:
            if tictactoe[2][0] == '-':
                tictactoe[2][0] = 'O'
                return True
        if tictactoe[1][1] != '-' and tictactoe[1][1] == tictactoe[2][0]:
            if tictactoe[0][2] == '-':
                tictactoe[0][2] = 'O'
                return True

############################################################

def checkrow_X(tictactoe):
    for i in range(len(tictactoe)):
        if '-' in tictactoe[i]:
            for j in range(len(tictactoe[i])):
                if tictactoe[i].count('X') == 2:
                    if tictactoe[i][j] == '-':
                        tictactoe[i][j] = 'O'
                        return True

############################################################

def checkcolumn_X(tictactoe:list):
    for i in range(len(tictactoe)):
            if tictactoe[0][i] == 'X' and tictactoe[0][i] == tictactoe[1][i]:
                if tictactoe[2][i] == '-':
                    tictactoe[2][i] = 'O'
                    return True
            if tictactoe[1][i] == 'X' and tictactoe[1][i] == tictactoe[2][i]:
                if tictactoe[0][i] == '-':
                    tictactoe[0][i] = 'O'
                    return True
            if tictactoe[0][i] == 'X' and tictactoe[0][i] == tictactoe[2][i]:
                if tictactoe[1][i] == '-':
                    tictactoe[1][i] = 'O'
                    return True

############################################################

def  check3slots(tictactoe: list):
    if tictactoe[1][1] == 'O':
        if tictactoe[0][0] == 'X' and tictactoe[2][2] == 'X' or tictactoe[0][2] == 'X' and tictactoe [2][0] == 'X':
            if tictactoe[0][1] == '-':
                tictactoe[0][1] = 'O'
                return True
            if tictactoe[2][1] == '-':
                tictactoe[2][1] = 'O'
                return True
        if tictactoe[0][0] == 'X' and tictactoe[1][2] == 'X' or tictactoe[0][1] == 'X' and tictactoe[2][2] == 'X' or tictactoe[0][1] == 'X' and tictactoe[1][2] == 'X':
            if tictactoe[0][2] == '-':
                tictactoe[0][2] = 'O'
                return True
        if tictactoe[0][2] == 'X' and tictactoe[1][0] == 'X' or tictactoe[0][1] == 'X' and tictactoe[2][0] == 'X' or tictactoe[0][1] == 'X' and tictactoe[1][0] == 'X' :#or tictactoe[0][1] == 'X' and tictactoe[2][1] or tictactoe[1][0] == 'X' and tictactoe[1][2]:
            if tictactoe[0][0] == '-':
                tictactoe[0][0] = 'O'
                return True
        if tictactoe[0][2] == 'X' and tictactoe[2][1] == 'X' or tictactoe[1][2] == 'X' and tictactoe[2][0] == 'X' or tictactoe[1][2] == 'X' and tictactoe[2][1] == 'X':
            if tictactoe[2][2] == '-':
                tictactoe[2][2] = 'O'
                return True
        if tictactoe[0][0] == 'X' and tictactoe[2][1] == 'X' or tictactoe[1][0] == 'X' and tictactoe[2][2] == 'X' or tictactoe[1][0] == 'X' and tictactoe[2][1] == 'X':
            if tictactoe[2][0] == '-':
                tictactoe[2][0] = 'O'
                return True

    for i in range(len(tictactoe)):
        for j in range(len(tictactoe[i])):
            if tictactoe[i][j] == '-':
                tictactoe[i][j] = 'O'
                return True
