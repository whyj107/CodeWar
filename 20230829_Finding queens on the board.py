# Finding queens on the board
# https://www.codewars.com/kata/64060d8ab2dd990058b7f8ee/train/python

# 나의 풀이
# queen : 3n-2
# total - queen : n^2 - (3n-2)
#               : (n-2)(n-1)
def queens(n):
    return (n-2)*(n-1) if n > 0 else 0

# 다른 사람의 풀이
def queens1(n):
    return n>0 and (n-1)*(n-2)

print(queens(0), 0)
print(queens(1), 0)
print(queens(2), 0)
print(queens(3), 2)
print(queens(4), 6)
print(queens(5), 12)
print(queens(6), 20)
print(queens(20), 342)
print(queens(33), 992)
print(queens(50), 2352)