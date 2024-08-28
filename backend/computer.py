# # Constants for player symbols
# PLAYER = 'X'
# COMPUTER = 'O'

# def computer(squares):
#     if squares[1][1] == '':
#         squares[1][1] = COMPUTER
#         return
    
#     if attempt_to_win(squares, COMPUTER):
#         return
    
#     if attempt_to_block(squares, PLAYER):
#         return

#     make_optimal_move(squares)

# def attempt_to_win(squares, symbol):
#     return check_row(squares, symbol) or check_column(squares, symbol) or check_diagonals(squares, symbol)

# def attempt_to_block(squares, symbol):
#     return check_row(squares, symbol) or check_column(squares, symbol) or check_diagonals(squares, symbol)

# def check_row(squares, symbol):
#     for i in range(len(squares)):
#         if squares[i].count(symbol) == 2 and '' in squares[i]:
#             squares[i][squares[i].index('')] = COMPUTER
#             return True
#     return False

# def check_column(squares, symbol):
#     for i in range(len(squares)):
#         column = [squares[j][i] for j in range(len(squares))]
#         if column.count(symbol) == 2 and '' in column:
#             squares[column.index('')][i] = COMPUTER
#             return True
#     return False

# def check_diagonals(squares, symbol):
#     diag1 = [squares[i][i] for i in range(len(squares))]
#     diag2 = [squares[i][len(squares)-1-i] for i in range(len(squares))]

#     if diag1.count(symbol) == 2 and '' in diag1:
#         squares[diag1.index('')][diag1.index('')] = COMPUTER
#         return True

#     if diag2.count(symbol) == 2 and '' in diag2:
#         squares[diag2.index('')][len(squares)-1-diag2.index('')] = COMPUTER
#         return True

#     return False

# def make_optimal_move(squares):
#     # Make an optimal move when the computer can't win or block the player
#     for i in range(len(squares)):
#         for j in range(len(squares[i])):
#             if squares[i][j] == '':
#                 squares[i][j] = COMPUTER
#                 return True
#     return False




def computer(squares):
    print(111)
    if squares[1][1] == '':
        squares[1][1] = 'O'
        return
    elif squares[0][0] == '' and squares[1][1] == 'X':
        squares[0][0] = 'O'
        return

    if checkrow_O(squares) == True:
        return
    if checkcolumn_O(squares) == True:
        return
    if checkcdiagonally(squares) == True:
        return
    if checkrow_X(squares) == True:
        return
    if checkcolumn_X(squares) == True:
        return
    if check3slots(squares) == True:
        return

############################################################

def checkrow_O(squares):
    print(222)
    for i in range(len(squares)):
        if '' in squares[i]:
            for j in range(len(squares[i])):
                if squares[i].count('O') == 2 or squares[i].count('X') == 2:
                    if squares[i][j] == '':
                        squares[i][j] = 'O'
                        return True

############################################################

def checkcolumn_O(squares:list):
    print(333)
    for i in range(len(squares)):
            if squares[0][i] == 'O' and squares[0][i] == squares[1][i] or squares[0][i] == 'X' and squares[0][i] == squares[1][i]:
                if squares[2][i] == '':
                    squares[2][i] = 'O'
                    return True
            if squares[1][i] == 'O' and squares[1][i] == squares[2][i] or squares[1][i] == 'X' and squares[1][i] == squares[2][i]:
                if squares[0][i] == '':
                    squares[0][i] = 'O'
                    return True
            if squares[0][i] == 'O' and squares[0][i] == squares[2][i] or squares[0][i] == 'X' and squares[0][i] == squares[2][i]:
                if squares[1][i] == '':
                    squares[1][i] = 'O'
                    return True

############################################################

def checkcdiagonally(squares: list):
    print(444)
#checkcdiagonally_from left to right
    if squares[0][0] == squares[1][1]: # if... == 'O'
        if squares[2][2] == '':
            squares[2][2] = 'O'
            return True
    if squares[1][1] != '' and squares[1][1] == squares[2][2]:
        if squares[0][0] == '':
            squares[0][0] = 'O'
            return True
        else:
            if squares[0][2] == '':
                squares[0][2] = 'O'
                return True
            2
            if squares[0][1] == '':
                squares[0][1] = 'O'
                return True

#checkcdiagonally_from righ to tleft
    if squares[0][2] != '' and squares[0][2] == squares[1][1]:
        if squares[2][0] == '':
            squares[2][0] = 'O'
            return True
    if squares[1][1] != '' and squares[1][1] == squares[2][0]:
        if squares[0][2] == '':
            squares[0][2] = 'O'
            return True

############################################################

def checkrow_X(squares):
    print(555)
    for i in range(len(squares)):
        if '' in squares[i]:
            for j in range(len(squares[i])):
                if squares[i].count('X') == 2:
                    if squares[i][j] == '':
                        squares[i][j] = 'O'
                        return True

############################################################

def checkcolumn_X(squares:list):
    print(666)
    for i in range(len(squares)):
            if squares[0][i] == 'X' and squares[0][i] == squares[1][i]:
                if squares[2][i] == '':
                    squares[2][i] = 'O'
                    return True
            if squares[1][i] == 'X' and squares[1][i] == squares[2][i]:
                if squares[0][i] == '':
                    squares[0][i] = 'O'
                    return True
            if squares[0][i] == 'X' and squares[0][i] == squares[2][i]:
                if squares[1][i] == '':
                    squares[1][i] = 'O'
                    return True

############################################################

def  check3slots(squares: list):
    print(777)
    if squares[1][1] == 'O':
        if squares[0][0] == 'X' and squares[2][2] == 'X' or squares[0][2] == 'X' and squares [2][0] == 'X':
            if squares[0][1] == '':
                squares[0][1] = 'O'
                return True
            if squares[2][1] == '':
                squares[2][1] = 'O'
                return True
        if squares[0][0] == 'X' and squares[1][2] == 'X' or squares[0][1] == 'X' and squares[2][2] == 'X' or squares[0][1] == 'X' and squares[1][2] == 'X':
            if squares[0][2] == '':
                squares[0][2] = 'O'
                return True
        if squares[0][2] == 'X' and squares[1][0] == 'X' or squares[0][1] == 'X' and squares[2][0] == 'X' or squares[0][1] == 'X' and squares[1][0] == 'X' :#or tictactoe[0][1] == 'X' and tictactoe[2][1] or tictactoe[1][0] == 'X' and tictactoe[1][2]:
            if squares[0][0] == '':
                squares[0][0] = 'O'
                return True
        if squares[0][2] == 'X' and squares[2][1] == 'X' or squares[1][2] == 'X' and squares[2][0] == 'X' or squares[1][2] == 'X' and squares[2][1] == 'X':
            if squares[2][2] == '':
                squares[2][2] = 'O'
                return True
        if squares[0][0] == 'X' and squares[2][1] == 'X' or squares[1][0] == 'X' and squares[2][2] == 'X' or squares[1][0] == 'X' and squares[2][1] == 'X':
            if squares[2][0] == '':
                squares[2][0] = 'O'
                return True

    for i in range(len(squares)):
        for j in range(len(squares[i])):
            if squares[i][j] == '':
                squares[i][j] = 'O'
                return True
