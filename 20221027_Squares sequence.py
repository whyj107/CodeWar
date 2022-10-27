# Squares sequence
# https://www.codewars.com/kata/5546180ca783b6d2d5000062/train/python

# 나의 풀이
def squares(x, n):
    if n < 1: return []
    result = [x]
    for i in range(1, n):
        result.append(pow(result[-1], 2))
    return result

# 다른 사람의 풀이
def squares1(x,n):
    return [x**(2**i) for i in range(n)]

from itertools import accumulate, repeat
def squares2(x, n):
    return list(accumulate(repeat(x, n), lambda a, _: a * a))

print(squares(2, 5), [2, 4, 16, 256, 65536])
print(squares(3, 3), [3, 9, 81])
print(squares(5, 3), [5, 25, 625])
print(squares(10, 4), [10, 100, 10000, 100000000])
print(squares(2, 0), [])
print(squares(2, -4), [])