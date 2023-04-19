# The @ Operator
# https://www.codewars.com/kata/631f0c3a0b9cb0de6ded0529/train/python

# a @ b = (a + b) + (a - b) + (a * b) + (a // b)
# 나의 풀이
def evaluate(equation):
    a,b = 0, 0
    tmp = True
    for i in equation.split():
        if i == '@': continue
        if tmp:
            a = int(i)
            tmp = False
        else:
            b = int(i)
            a = solve(a, b)
            if a is None: return None
    return a

def solve(a, b):
    return (a+b)+(a-b)+(a*b)+(a//b) if b else None

# 다른 사람의 풀이
from functools import reduce
def evaluate1(equation):
    try:
        return reduce(lambda a, b: a * (b + 2) + a // b, map(int, equation.split(' @ ')))
    except ZeroDivisionError:
        pass

tests = [
    ['1 @ 1', 4],
    ['3 @ 2', 13],
    ['6 @ 9', 66],
    ['4 @ -4', -9],
    ['1 @ 1 @ -4', -9],
    ['2 @ 2 @ 2', 40],
    ['0 @ 1 @ 2', 0],
    ['5 @ 0', None]
]
for equation, answer in tests:
    print(evaluate(equation), answer)