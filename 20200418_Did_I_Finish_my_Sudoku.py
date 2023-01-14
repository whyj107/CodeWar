# 문제
# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
# If the board is valid return 'Finished!', otherwise return 'Try again!'

# 입력 == 출력
# test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
#
# test.assert_equals(done_or_not([
#                          [1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');

# My Code
from itertools import product
def done_or_not(board):
    chk = {i for i in range(1, 10)}
    # 가로
    for r in range(9):
        if {*board[r]} != chk: 
            return 'Try again!'
    # 세로
    for c in zip(*board):
        if {*c} != chk:
            return 'Try again!'
    # 3x3
    for r, c in product([0, 3, 6], repeat=2):
        three = sum([board[r+i][c:c+3] for i in range(3)], [])
        if {*three} != chk: 
            return 'Try again!'
    return 'Finished!'

# Warrios
import numpy as np
def done_or_not_(aboard):  # board[i][j]
    board = np.array(aboard)

    rows = [board[i, :] for i in range(9)]
    cols = [board[:, j] for j in range(9)]
    sqrs = [board[i:i + 3, j:j + 3].flatten() for i in [0, 3, 6] for j in [0, 3, 6]]

    for view in np.vstack((rows, cols, sqrs)):
        if len(np.unique(view)) != 9:
            return 'Try again!'

    return 'Finished!'

if __name__ == '__main__':
    answer = done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                          [4, 9, 8, 2, 6, 1, 3, 7, 5],
                          [7, 5, 6, 3, 8, 4, 2, 1, 9],
                          [6, 4, 3, 1, 5, 8, 7, 9, 2],
                          [5, 2, 1, 7, 9, 3, 8, 4, 6],
                          [9, 8, 7, 4, 2, 6, 5, 3, 1],
                          [2, 1, 4, 9, 3, 5, 6, 8, 7],
                          [3, 6, 5, 8, 1, 7, 9, 2, 4],
                          [8, 7, 9, 6, 4, 2, 1, 3, 5]])
    print(answer)
