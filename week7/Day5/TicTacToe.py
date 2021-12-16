theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def play():

    turn = "X"
    count = 0

    for i in range(10):
        printBoard(theBoard)
        player_position = input("Where do you want to position your " + turn + " ?")

        if theBoard[player_position] == ' ':
            theBoard[player_position] = turn
            count += 1

    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

        if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(" **** " + turn + " won. ****")
            return

    if count == 9:
        print("\nGame Over.\n")
        print("It's a Tie!!")

    if turn == "X":
        turn = "O"
    else:
        turn = "O"


play()