import pytest


# Create your tests here.
def test_edge_one():
    input = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]
    ret, _ = solve_and_check(input)
    assert ret == True


def test_use_one():
    input = [
    [1, 2, 3, 4, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]
    ret, _ = solve_and_check(input)
    assert ret == True


def test_use_two():
    input = [
    [1, 2, 3, 4, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 5, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 7, -1, -1, -1, -1, 6, -1],
    [-1, -1, -1, -1, 9, -1, -1, -1, -1]
    ]
    ret, _ = solve_and_check(input)
    assert ret == True


def test_use_three():
    input = [
    [1, 2, 3, 4, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 5, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 7, -1, -1, -1, -1, 6, -1],
    [-1, -1, -1, -1, 9, -1, -1, -1, -1]
    ]
    expected = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 1, 4, 9, 6, 7, 5, 3, 8],
        [3, 6, 5, 2, 1, 8, 9, 4, 7],
        [9, 7, 8, 3, 4, 5, 6, 1, 2],
        [5, 3, 1, 6, 7, 2, 8, 9, 4],
        [8, 9, 7, 5, 3, 4, 2, 6, 1],
        [6, 4, 2, 8, 9, 1, 3, 7, 5]
    ]
    ret, board = solve_and_check(input)
    assert ret == True and board == expected


def test_use_four():
    input = [
    [-1, -1, 2, -1, -1, -1, -1, -1, 6],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, -1, -1, -1],
    [-1, -1, -1, 4, -1, -1, -1, -1, 5],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 8, -1, -1, -1, -1],
    [-1, 7, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 9, -1, -1, -1]
    ]
    expected = [
        [1, 3, 2, 5, 4, 7, 8, 9, 6],
        [4, 5, 6, 1, 9, 8, 2, 3, 7],
        [7, 8, 9, 3, 2, 6, 1, 5, 4],
        [2, 1, 7, 4, 6, 3, 9, 8, 5],
        [3, 4, 8, 9, 1, 5, 6, 7, 2],
        [6, 9, 5, 7, 8, 2, 3, 4, 1],
        [8, 7, 1, 2, 3, 4, 5, 6, 9],
        [9, 6, 4, 8, 5, 1, 7, 2, 3],
        [5, 2, 3, 6, 7, 9, 4, 1, 8]
    ]
    ret, board = solve_and_check(input)
    assert ret == True and board == expected


def test_use_five():
    input = [
    [1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 2, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 3, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 4, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 6, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 7, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 8, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 9]
    ]
    expected = [
        [1, 4, 5, 2, 3, 7, 6, 9, 8],
        [6, 2, 7, 1, 8, 9, 3, 4, 5],
        [8, 9, 3, 5, 6, 4, 1, 2, 7],
        [2, 1, 6, 4, 7, 8, 9, 5, 3],
        [3, 7, 4, 9, 5, 1, 8, 6, 2],
        [5, 8, 9, 3, 2, 6, 4, 7, 1],
        [4, 5, 1, 8, 9, 2, 7, 3, 6],
        [9, 6, 2, 7, 1, 3, 5, 8, 4],
        [7, 3, 8, 6, 4, 5, 2, 1, 9]
    ]
    ret, board = solve_and_check(input, verbose=True)
    assert ret == True and board == expected













# put here to keep __init__.py files simple and for the web app only
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
          

def solve(row, col, board, count=0):
    count += 1

    # check for 'no' solution
    if (count > 1000000):
        count = 0
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

def solve_and_check(board, verbose=False):
    solve(0,0,board)
    ret = check_sudoku(board)
    if verbose:
        for i in range(9):
            print(board[i])
        print(f"Valid Sudoku:          {check_sudoku(board)}")
    return ret, board