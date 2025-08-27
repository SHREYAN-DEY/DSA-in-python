import collections

def validSudoku(board):
    row = collections.defaultdict(set)
    col = collections.defaultdict(set)
    square = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in row[r] or 
                board[r][c] in col[c] or 
                board[r][c] in square[(r//3, c//3)]):
                return False
            else:
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
    return True
            

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

ty = validSudoku(board)
print(ty)