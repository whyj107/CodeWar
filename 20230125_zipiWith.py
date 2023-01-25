# zipWith
# https://www.codewars.com/kata/5825792ada030e9601000782/train/python

# 나의 풀이
def zip_with(fn, a1, a2):
    return [fn(i, j) for i, j in zip(a1, a2)]

# 다른 사람의 풀이
def zip_with1(fn, a1, a2):
    return list(map(fn, a1, a2))


def add(x, y): return x+y
def sub(x, y): return x-y
def mul(x, y): return x*y

print(zip_with(add, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1]), [6, 6, 6, 6, 6, 6])
print(zip_with(add, [0, 1, 2, 3, 4], [6, 5, 4, 3, 2, 1]), [6, 6, 6, 6, 6])
print(zip_with(add, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2]), [6, 6, 6, 6, 6])
print(zip_with(pow, [10, 10, 10, 10], [0, 1, 2, 3]), [1, 10, 100, 1000])
print(zip_with(max, [1, 4, 7, 1, 4, 7], [4, 7, 1, 4, 7, 1]), [4, 7, 7, 4, 7, 7])
print(zip_with(add, [0, 1, 2, 3], [0, 1, 2, 3]), [0, 2, 4, 6])
print(zip_with(add, [0, 1, 2, 3], [0, 1, 2, 3]), [0, 2, 4, 6])
print(zip_with(pow, [10, 10, 10, 10, 10, 10, 10], [0, 1, 2, 3, 4, 5, 6]), [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6])
print(zip_with(sub, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1]), [-6, -4, -2, 0, 2, 4])
print(zip_with(mul, ["a", "b", "c", "d", "e", "f"], [6, 5, 4, 3, 2, 1]), ["aaaaaa", "bbbbb", "cccc", "ddd", "ee", "f"])
