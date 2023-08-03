# Find Multiples of a Number
# https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python

# 나의 풀이
def find_multiples(integer, limit):
    r = []
    idx = 1
    while integer*idx <= limit:
        r.append(integer*idx)
        idx += 1
    return r

# 다른 사람의 풀이
def solve(i, l):
    return range(i, l+1, i)