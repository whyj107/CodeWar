# Matrix Transpose
# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python

# 나의 풀이
def transpose(matrix):
    return [list(i) for i in zip(*matrix)]

# 다른 사람의 풀이
def transpose1(matrix):
    return list(map(list, zip(*matrix)))

import numpy as np
def transpose2(matrix):
    return np.transpose(np.matrix(matrix)).tolist()

print(transpose([[1]]), [[1]])
print(transpose([[1, 2, 3]]), [[1], [2], [3]])
print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
print(transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])