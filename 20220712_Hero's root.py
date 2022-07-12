# Hero's root
# https://www.codewars.com/kata/55efecb8680f47654c000095/train/python

# 나의 풀이
from math import floor
def int_rac(n, guess):
    cnt = 0
    while True:
        cnt += 1
        new_n = floor((guess+(n/guess))/2)
        if abs(guess - new_n) < 1:
            break
        guess = new_n
    return cnt

# 다른 사람의 풀이
def int_rac1(n, guess):
    x = guess
    cnt = 1
    while True:
        newx = (x + n // x) // 2
        if abs(x - newx) < 1:
            return cnt
        x = newx
        cnt += 1

print(int_rac(25, 1), 4)
print(int_rac(125348, 300), 3)