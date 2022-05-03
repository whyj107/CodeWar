# Bingo(Or Not)
# https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/train/python

# 나의 풀이
def bingo(array):
    bingo_ = [2, 9, 14, 7, 15]
    result = sum([b in array for b in bingo_])
    return "WIN" if result == len(bingo_) else "LOSE"

# 다른 사람의 풀이
def bingo1(array):
    return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"

print(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE")
print(bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE")
print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN")
print(bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN")