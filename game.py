from helpers import displayBoard, checkDraw, checkWin
from ai_helpers import getComputerMove

# Game is playing
playing = True
while playing:
    in_game = True
    board = [' '] * 9
    print('Would you like to go first or second? (1/2)')
    if input() == '1':
        # If player goes first he gets a '0' marker
        playerMarker = '0'
    else:
        # If player goes second he gets an 'X' marker
        playerMarker = 'X'
        
    displayBoard(board)
    
    # when in the game
    while in_game:
        # If the player goes first, get his input
        if playerMarker == '0':
            print('Player go: (0-8)')
            move = int(input())
            if board[move] != ' ':
                print('Invalid move!')
                continue
        else:
            # Otherwise computer goes
            move = getComputerMove(board)
        board[move] = playerMarker
        # Check if any player has won the game
        if checkWin(board, playerMarker):
            in_game = False
            displayBoard(board)
            if playerMarker == '0':
                print('Noughts won!')
            else:
                print('Crosses won!')
            continue
        # Check if there was a draw
        if checkDraw(board):
            in_game = False
            displayBoard(board)
            print('It was a draw!')
            continue
        displayBoard(board)
        # Swich markers
        if playerMarker == '0':
            playerMarker = 'X'
        else:
            playerMarker = '0'

    # If game is over ask to play again
    print('Type y to keep playing')
    inp = input()
    if inp != 'y' and inp != 'Y':
        playing = False
