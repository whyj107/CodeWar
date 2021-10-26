# Pairs of integers from 0 to n
# https://www.codewars.com/kata/588e27b7d1140d31cb000060/train/python

# 나의 풀이
def generate_pairs(n):
    return sorted([[j, i] for i in range(n+1) for j in range(i+1)])

# 다른 사람의 풀이
def generate_pairs1(n):
    return [[i, j] for i in range(n+1) for j in range(i, n+1)]

print(generate_pairs(2))
print([[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]])
print(generate_pairs(0), [[0, 0]])