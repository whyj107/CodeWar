# Reverse polish notation calculator
# https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/python

# 나의 풀이
ope = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
def calc(expr):
    expr = expr.split()
    if len(expr) > 3:
        if expr[-2] in ope.keys():
            a = expr[0]
            b = calc(' '.join(expr[1:-1]))
        else:
            a = calc(' '.join(expr[:-2]))
            b = expr[-2]
        return ope[expr[-1]](float(a), float(b))
    elif len(expr) == 3:
        return ope[expr[2]](float(expr[0]), float(expr[1]))
    elif len(expr) == 1:
        return float(expr[0])
    else: return 0

# 다른 사람의 풀이
import operator
def calc1(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

print(calc(""), 0)
print(calc("3"), 3)
print(calc("3.5"), 3.5)
print(calc("1 3 +"), 4)
print(calc("1 3 *"), 3)
print(calc("1 3 -"), -2)
print(calc("4 2 /"), 2)
print(calc("5 1 2 + 4 * + 3 -"), 14)