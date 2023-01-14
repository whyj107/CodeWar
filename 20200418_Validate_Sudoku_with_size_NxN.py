# 문제
# Given a Sudoku data structure with size NxN, N > 0
# and √N == integer, write a method to validate if it has been filled out correctly.

# 입력 == 출력
# goodSudoku2 = Sudoku([
#   [1,4, 2,3],
#   [3,2, 4,1],
#
#   [4,1, 3,2],
#   [2,3, 1,4]
# ])
# badSudoku2 = Sudoku([
#   [1,2,3,4,5],
#   [1,2,3,4],
#   [1,2,3,4],
#   [1]
# ])

# My Code
from itertools import product
class Sudoku(object):
    def __init__(self, data):
        self.data = data
        # N 구하기
        self.n = max(len(i) for i in self.data)
        # 사각형 크기
        self.s_l = int(self.n**0.5)
        self.nums = set(range(1, self.n + 1))

    def is_valid(self):
        # 사이즈 검사
        if not all([len(i) == self.n for i in self.data]): return False

        # 데이터 타입 검사
        if not all([True if type(j) == type(1) else False for i in self.data for j in i]):
            return False
    
        # 가로줄 검사
        if not all([set(i) == self.nums for i in self.data]): return False

        # 세로줄 검사
        if not all([set(i) == self.nums for i in zip(*self.data)]): return False

        squares = [set(self.data[x+i][y+j]
                    for x, y in product(range(0, self.s_l), repeat=2)) == self.nums
                    for i, j in product(range(0, self.n, self.s_l), repeat=2)]
        # 사각형 검사
        if not all(squares): return False

        return True


if __name__=='__main__':
    goodSudoku2 = Sudoku([[1, 4, 2, 3],
                          [3, 2, 4, 1],
                          [4, 1, 3, 2],
                          [2, 3, 1, 4]])
    print(goodSudoku2.is_valid())
