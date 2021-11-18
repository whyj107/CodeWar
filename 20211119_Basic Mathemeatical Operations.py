# Basic Mathematical Operations
# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

# 나의 풀이
def basic_op(operator, value1, value2):
    dic = {'+': lambda x, y: x+y, '-': lambda x, y: x-y,
           '*': lambda x, y: x*y, '/': lambda x, y: x/y}
    return dic[operator](value1, value2)

# 다른 사람의 풀이
def basic_op1(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

def basic_op2(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

print(basic_op('+', 4, 7), 11)
print(basic_op('-', 15, 18), -3)
print(basic_op('*', 5, 5), 25)
print(basic_op('/', 49, 7), 7)