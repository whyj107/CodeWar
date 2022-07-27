# Simple Game
# https://www.codewars.com/kata/59831e3575ca6c8aea00003a/train/python

# 나의 풀이
def game(n, m):
    return ['second', 'first'][n % 2 and (m > 2)]

# 다른 사람의 풀이
def game1(x, y):
    return 'second' if y == 2 else 'first' if x % 2 and y % 2 == 0 or x % 2 else 'second'

print(game(3, 7), 'first')
print(game(6, 12), 'second')
print(game(2, 4), 'second')
