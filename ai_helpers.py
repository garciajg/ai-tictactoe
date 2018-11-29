from helpers import checkWin

def getBoardCopy(board):
    """
    This creates a duplicate of the board.
    When testing moves we don't want to change
    the actual board
    """
    dup_board = []
    for j in board:
        dup_board.append(j)
    return dup_board

def testWinMove(board, mark, index):
    board_copy = getBoardCopy(board)
    board_copy[index] = mark
    return checkWin(board_copy, mark)

def getComputerMove(board):
    # Check computer win moves
    for i in range(0, 9):
        if board[i] == " " and testWinMove(board, "X", i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if board[i] == " " and testWinMove(board, "0", i):
            return i
    # Check computer fork opportunities
    for i in range(0, 9):
        if board[i] == " " and testForkMove(board, "X", i):
            return i
    # Check player fork opportunities
    player_forks = 0
    for i in range(0, 9):
        if board[i] == " " and testForkMove(board, "0", i):
            player_forks += 1
            temp_move = i
    if player_forks == 1:
        return temp_move
    elif player_forks == 2:
        for j in [1,3,5,7]:
            if b[j] == " ":
                return j
    # Play a corner
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i
    # Play center
    if board[4] == " ":
        return 4
    # Play a side
    for i in [1, 3, 5, 7]:
        if board[i] == " ":
            return i
    
def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    b_copy = getBoardCopy(b)
    b_copy[i] = mark
    winning_moves = 0
    for j in range(0,9):
        if testWinMove(b_copy, mark, i) and b_copy[i] == " ":
            winning_moves += 1
    return winning_moves >= 2



    