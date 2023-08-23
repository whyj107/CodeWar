# Breaking chocolate problem
# https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python

# 나의 풀이
def break_chocolate(n, m):
    return max(0, n*m-1)

print(break_chocolate(5, 5), 24)
print(break_chocolate(7, 4), 27)
print(break_chocolate(1, 1), 0)
print(break_chocolate(0, 0), 0)
print(break_chocolate(6, 1), 5)