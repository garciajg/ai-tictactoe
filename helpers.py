def displayBoard(board):
    print("     |     |") # There's 5 spaces in between lines
    print("  {0}  |  {1}  |  {2}  |".format(board[0], board[1], board[2])) # there's two spaces before and after the mark
    print("     |     |")
    print("-----------------") # 12  dashes total
    print("     |     |")
    print("  {0}  |  {1}  |  {2}  |".format(board[3], board[4], board[5]))
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  {0}  |  {1}  |  {2}  |".format(board[6], board[7], board[8]))
    print("     |     |")

def checkWin(board, marker):
    """
    This method cheack if any player has won the game by
    checking each row from left to right,
    each column from top to bottom, and 
    from corner to corner.
    """
    return (
                (board[0] == marker and board[1] == marker and board[2] == marker) or # Vertical line top
                (board[3] == marker and board[4] == marker and board[5] == marker) or # Vertical line middle
                (board[6] == marker and board[7] == marker and board[8] == marker) or # Vertical line bottom
                (board[0] == marker and board[3] == marker and board[6] == marker) or # Horizontal line left
                (board[1] == marker and board[4] == marker and board[7] == marker) or # Horizontal line middle
                (board[2] == marker and board[5] == marker and board[8] == marker) or # Horizontal line right
                (board[0] == marker and board[4] == marker and board[8] == marker) or # Line from top left to bottom right
                (board[2] == marker and board[4] == marker and board[6] == marker)    # Line from top right to bottom left
            )

def checkDraw(board):
    """
    Checks for any blank spaces when no player has won yet
    """
    return " " not in board
    
