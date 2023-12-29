from computer import computer

############################################################


def make_step(squares, vsAI):
    if vsAI == '1':
        return win(squares)
    else:
        if win(squares):
            return win(squares)
        computer(squares)

############################################################

def win(squares):
    for i in range(len(squares)):
        if squares[i][0] != '' and squares[i][0] == squares[i][1] == squares[i][2]:  # row
            return squares[i][0]

    for i in range(len(squares)):
        if squares[0][i] != '' and squares[0][i] == squares[1][i] == squares[2][i]:  # column
            return squares[0][i]

    if squares[0][0] != '' and squares[0][0] == squares[1][1] == squares[2][2]:  # diagonal
        return squares[0][0]
    elif squares[0][2] != '' and squares[0][2] == squares[1][1] == squares[2][0]:  # diagonal
        return squares[0][2]

    if all(cell != '' for row in squares for cell in row):
        return 'המשחק הסתיים בתיקו'
    
    return False            