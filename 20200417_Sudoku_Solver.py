# 문제
# Write a function that will solve a 9x9 Sudoku puzzle.
# The function will take one argument consisting of the 2D puzzle array,
# with the value 0 representing an unknown square.
# The Sudokus tested against your function will be "easy"
# (i.e. determinable; there will be no need to assume and test possibilities on unknowns)
# and can be solved with a brute-force approach.
# For Sudoku rules, see the Wikipedia article.

# 입력 == 출력
# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]
#
# solution = [[5,3,4,6,7,8,9,1,2],
#             [6,7,2,1,9,5,3,4,8],
#             [1,9,8,3,4,2,5,6,7],
#             [8,5,9,7,6,1,4,2,3],
#             [4,2,6,8,5,3,7,9,1],
#             [7,1,3,9,2,4,8,5,6],
#             [9,6,1,5,3,7,2,8,4],
#             [2,8,7,4,1,9,6,3,5],
#             [3,4,5,2,8,6,1,7,9]]

# My Code
def sudoku(puzzle):
    # 0인 것들 찾아서 저장
    board = [(r, c) for r in range(9) for c in range(9) if not puzzle[r][c]]
    for row, col in board:
        # 0: 0~2, 3: 3~5, 6: 6~8
        rr, cc = (row // 3) * 3, (col // 3) * 3
        
        # 가로, 세로, 3x3 숫자 확인
        sero = {puzzle[r][col] for r in range(9)}
        garo = {puzzle[row][c] for c in range(9)}
        three = {puzzle[rr+r][cc+c] for r in range(3) for c in range(3)}

        # 숫자 확인
        use = {1,2,3,4,5,6,7,8,9} - (sero | garo | three)

        # 1개 비면 그 숫자 채워 넣기
        if len(use) == 1:
            puzzle[row][col] = use.pop()
            # 재귀로 계속해서 찾음
            return sudoku(puzzle)
    return puzzle

# -------------------------------------------------------------------------------------------------
if __name__=='__main__':
    answer = sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                     [6, 0, 0, 1, 9, 5, 0, 0, 0],
                     [0, 9, 8, 0, 0, 0, 0, 6, 0],
                     [8, 0, 0, 0, 6, 0, 0, 0, 3],
                     [4, 0, 0, 8, 0, 3, 0, 0, 1],
                     [7, 0, 0, 0, 2, 0, 0, 0, 6],
                     [0, 6, 0, 0, 0, 0, 2, 8, 0],
                     [0, 0, 0, 4, 1, 9, 0, 0, 5],
                     [0, 0, 0, 0, 8, 0, 0, 7, 9]])
    print(answer)
    puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 3, 6, 0, 0, 0, 0, 0],
              [0, 7, 0, 0, 9, 0, 2, 0, 0],
              [0, 5, 0, 0, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 4, 5, 7, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 3, 0],
              [0, 0, 1, 0, 0, 0, 0, 6, 8],
              [0, 0, 8, 5, 0, 0, 0, 1, 0],
              [0, 9, 0, 0, 0, 0, 4, 0, 0]]
    answer = sudoku_(puzzle)
    print(answer)
