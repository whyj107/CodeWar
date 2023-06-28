# Alternating between three values
# https://www.codewars.com/kata/596776fbb4f24d0d82000141/train/python

# 나의 풀이
def f(x, a, b, c):
    return b if x==a else(c if x==b else a)

# 다른 사람의 풀이
def f1(x, a, b, c):
    return {a:b, b:c, c:a}[x]