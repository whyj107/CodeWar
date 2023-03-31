# Simple Fun #19: Count Black Cells
# https://www.codewars.com/kata/588475d575431d0a0e000023/train/python

# 나의 풀이
from math import gcd
def count_black_cells(h, w):
    return h+w+gcd(w, h)-2

print(count_black_cells(3, 4), 6)
print(count_black_cells(3, 3), 7)
print(count_black_cells(2, 5), 6)
print(count_black_cells(1, 1), 1)
print(count_black_cells(1, 2), 2)
print(count_black_cells(1, 239), 239)
print(count_black_cells(33, 44), 86)
print(count_black_cells(16, 8), 30)
print(count_black_cells(6666, 8888), 17774)