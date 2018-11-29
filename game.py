from helpers import displayBoard, checkDraw, checkWin
from ai_helpers import getComputerMove

# Game is playing
playing = True
while playing:
    in_game = True
    board = [' '] * 9
    print('Would you like to go first or second? (1/2)')
    if input() == '1':
        playerMarker = '0'
    else:
        playerMarker = 'X'
    displayBoard(board)

    while in_game:
        if playerMarker == '0':
            print('Player go: (0-8)')
            move = int(input())
            if board[move] != ' ':
                print('Invalid move!')
                continue
        else:
            move = getComputerMove(board)
        board[move] = playerMarker
        if checkWin(board, playerMarker):
            in_game = False
            displayBoard(board)
            if playerMarker == '0':
                print('Noughts won!')
            else:
                print('Crosses won!')
            continue
        if checkDraw(board):
            in_game = False
            displayBoard(board)
            print('It was a draw!')
            continue
        displayBoard(board)
        if playerMarker == '0':
            playerMarker = 'X'
        else:
            playerMarker = '0'

    print('Type y to keep playing')
    inp = input()
    if inp != 'y' and inp != 'Y':
        playing = False