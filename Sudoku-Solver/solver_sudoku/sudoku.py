array = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
]

def valid_placement(row, col, board):
    val = board[row][col]
    if (val == -1):
        return True
    # Check the row
    arr = board[row]
    for i, element in enumerate(arr):
        if (element == val and i != col):
            return False
    
    # Check the column
    for i in range(9):
        if (board[i][col] == val and i != row):
            return False
    
    # upper left
    if (row % 3 == 0 and col % 3 == 0):
        if (board[row+1][col+1] == val or board[row+1][col+2] == val or board[row+2][col+1] == val or board[row+2][col+2] == val):
            if (val != -1):
                return False

    # upper middle
    if (row % 3 == 0 and col % 3 == 1):
        if (board[row+1][col-1] == val or board[row+1][col+1] == val or board[row+2][col-1] == val or board[row+2][col+1] == val):
            if (val != -1):
                return False

    # upper right
    if (row % 3 == 0 and col % 3 == 2):
        if (board[row+1][col-2] == val or board[row+1][col-1] == val or board[row+2][col-2] == val or board[row+2][col-1] == val):
            if (val != -1):
                return False

    # middle  left
    if (row % 3 == 1 and col % 3 == 0):
        if (board[row-1][col+1] == val or board[row-1][col+2] == val or board[row+1][col+1] == val or board[row+1][col+2] == val):
            if (val != -1):
                return False

    # middle middle
    if (row % 3 == 1 and col % 3 == 1):
        if (board[row-1][col-1] == val or board[row-1][col+1] == val or board[row+1][col-1] == val or board[row+1][col+1] == val):
            if (val != -1):
                return False

    # middle right
    if (row % 3 == 1 and col % 3 == 2):
        if (board[row-1][col-2] == val or board[row-1][col-1] == val or board[row+1][col-2] == val or board[row+1][col-1] == val):
            if (val != -1):
                return False

    # lower left
    if (row % 3 == 2 and col % 3 == 0):
        if (board[row-2][col+1] == val or board[row-2][col+2] == val or board[row-1][col+1] == val or board[row-1][col+2] == val):
            if (val != -1):
                return False

    # lower middle
    if (row % 3 == 2 and col % 3 == 1):
        if (board[row-1][col-1] == val or board[row-1][col+1] == val or board[row-2][col-1] == val or board[row-2][col+1] == val):
            if (val != -1):
                return False
    
    # lower right
    if (row % 3 == 2 and col % 3 == 2):
        if (board[row-1][col-2] == val or board[row-1][col-1] == val or board[row-2][col-2] == val or board[row-2][col-1] == val):
            if (val != -1):
                return False
            
    # if all passed
    return True
          

def solve(row, col, board):
    if not hasattr(solve, "count"):
        solve.count = 0

    solve.count += 1

    # check for 'no' solution
    if (len(count) > 1000000):
        count = []
        return False
    
    # base case
    if (col == len(board[0])):
        col = 0
        row += 1
    # we have completed the board
    if (row == len(board)):
        return True
    
    # skip over cells with initial values
    if (board[row][col] != -1):
        return solve(row, col+1, board)
    
    # set value considering constraints
    for i in range(1, 10):
        board[row][col] = i
        if (valid_placement(row, col, board)):
            if (solve(row, col+1, board)):
                return True
    
    # set board value to empty
    board[row][col] = -1


def check_sudoku(board):
    for row in range(len(board[0])):
        for col in range(len(board)):
            if (not(valid_placement(row, col, board)) or board[row][col] == -1):
                return False
    
    return True

def solve_and_check(board, verbose=False, count=[]):
    solve(0,0,board, count)
    solve.count = 0
    ret = check_sudoku(board)
    if verbose:
        for i in range(9):
            print(board[i])
        print(f"Valid Sudoku:          {check_sudoku(board)}")
    return ret, board