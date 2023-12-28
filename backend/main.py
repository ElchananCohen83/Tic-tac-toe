import StepAndRool as sar

def main():
    print('היי חבר! אתה מוזמן לשחק איתי X/O מקווה שתהנה מכל רגע :)')
    print('אם אתה מעוניין לשחק עם חבר הקש 1, אם אתה מעוניין לשחק נגד המחשב הקש 2, ליציאה הקש 3')
    print("כדי לשחק עליך להכניס מספר (שורה) רווח ומספר(עמודה) לדוגמא: 2 3 (שים לב: על המספר להיות בין 1-3")

    def plays():
        count = 1
        while sar.win(tictactoe) != True:
            if sar.check_step(tictactoe,bool(count%2), play, count) != False:
                count += 1
                sar.print_board(tictactoe)
        print('מאוד נהנתי לשחק איתך :) , רוצה לשחק שוב? אם לא הקש 9')
        if input() != '9':
            main()

    plays()

main()