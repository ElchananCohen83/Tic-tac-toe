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
















# def computer(squares):

#     if not squares[1][1]:
#         squares[1][1] = 'O'
#         return
#     elif not squares[0][0]:
#         squares[0][0] = 'O'
#         return
    
#     if checkrow_O(squares) == True:
#         return
#     if checkcolumn_O(squares) == True:
#         return
#     if checkcdiagonally(squares) == True:
#         return
#     if checkrow_X(squares) == True:
#         return
#     if checkcolumn_X(squares) == True:
#         return
#     if check3slots(squares) == True:
#         return

# ############################################################

# def checkrow_O(squares):
#     for i in range(len(squares)):
#         if '' in squares[i]:
#             for j in range(len(squares[i])):
#                 if squares[i].count('O') == 2:
#                     if squares[i][j] == '':
#                         squares[i][j] = 'O'
#                         return True

# ############################################################

# def checkcolumn_O(squares:list):
#     for i in range(len(squares)):
#             if squares[0][i] == 'O' and squares[0][i] == squares[1][i]:
#                 if squares[2][i] == '':
#                     squares[2][i] = 'O'
#                     return True
#             if squares[1][i] == 'O' and squares[1][i] == squares[2][i]:
#                 if squares[0][i] == '':
#                     squares[0][i] = 'O'
#                     return True
#             if squares[0][i] and squares[0][i] == squares[2][i]:
#                 if squares[1][i] == '':
#                     squares[1][i] = 'O'
#                     return True

# ############################################################

# def checkcdiagonally(squares: list):
#     #checkcdiagonally_from left to right
#     if squares[0][0] == squares[1][1]: # if... == 'O'
#         if squares[2][2] == '':
#             squares[2][2] = 'O'
#             return True
#     if squares[1][1] and squares[1][1] == squares[2][2]:
#         if squares[0][0] == '':
#             squares[0][0] = 'O'
#             return True
#         else:
#             if squares[0][2] == '':
#                 squares[0][2] = 'O'
#                 return True
#             2
#             if squares[0][1] == '':
#                 squares[0][1] = 'O'
#                 return True

#     #checkcdiagonally_from righ to tleft
#         if squares[0][2] and squares[0][2] == squares[1][1]:
#             if squares[2][0] == '':
#                 squares[2][0] = 'O'
#                 return True
#         if squares[1][1] and squares[1][1] == squares[2][0]:
#             if squares[0][2] == '':
#                 squares[0][2] = 'O'
#                 return True

# ############################################################

# def checkrow_X(squares):
#     for i in range(len(squares)):
#         if '' in squares[i]:
#             for j in range(len(squares[i])):
#                 if squares[i].count('X') == 2:
#                     if squares[i][j] == '':
#                         squares[i][j] = 'O'
#                         return True

# ############################################################

# def checkcolumn_X(squares:list):
#     for i in range(len(squares)):
#             if squares[0][i] == 'X' and squares[0][i] == squares[1][i]:
#                 if squares[2][i] == '':
#                     squares[2][i] = 'O'
#                     return True
#             if squares[1][i] == 'X' and squares[1][i] == squares[2][i]:
#                 if squares[0][i] == '':
#                     squares[0][i] = 'O'
#                     return True
#             if squares[0][i] == 'X' and squares[0][i] == squares[2][i]:
#                 if squares[1][i] == '':
#                     squares[1][i] = 'O'
#                     return True

# ############################################################

# def  check3slots(squares: list):
#     if squares[1][1] == 'O':
#         if squares[0][0] == 'X' and squares[2][2] == 'X' or squares[0][2] == 'X' and squares [2][0] == 'X':
#             if squares[0][1] == '':
#                 squares[0][1] = 'O'
#                 return True
#             if squares[2][1] == '':
#                 squares[2][1] = 'O'
#                 return True
#         if squares[0][0] == 'X' and squares[1][2] == 'X' or squares[0][1] == 'X' and squares[2][2] == 'X' or squares[0][1] == 'X' and squares[1][2] == 'X':
#             if squares[0][2] == '':
#                 squares[0][2] = 'O'
#                 return True
#         if squares[0][2] == 'X' and squares[1][0] == 'X' or squares[0][1] == 'X' and squares[2][0] == 'X' or squares[0][1] == 'X' and squares[1][0] == 'X' :#or tictactoe[0][1] == 'X' and tictactoe[2][1] or tictactoe[1][0] == 'X' and tictactoe[1][2]:
#             if squares[0][0] == '':
#                 squares[0][0] = 'O'
#                 return True
#         if squares[0][2] == 'X' and squares[2][1] == 'X' or squares[1][2] == 'X' and squares[2][0] == 'X' or squares[1][2] == 'X' and squares[2][1] == 'X':
#             if squares[2][2] == '':
#                 squares[2][2] = 'O'
#                 return True
#         if squares[0][0] == 'X' and squares[2][1] == 'X' or squares[1][0] == 'X' and squares[2][2] == 'X' or squares[1][0] == 'X' and squares[2][1] == 'X':
#             if squares[2][0] == '':
#                 squares[2][0] = 'O'
#                 return True

#     for i in range(len(squares)):
#         for j in range(len(squares[i])):
#             if squares[i][j] == '':
#                 squares[i][j] = 'O'
#                 return True
