# Binary Calculator
# https://www.codewars.com/kata/546ba103f0cf8f7982000df4/train/python

# 나의 풀이
def calculate(n1, n2, o):
    n1 = int(n1, 2)
    n2 = int(n2, 2)
    dic = {"add":lambda x,y: x+y,
           "subtract":lambda x,y: x-y,
           "multiply":lambda x,y: x*y}
    r = bin(dic[o](n1, n2))
    return r.replace("0b", '')

# 다른 사람의 풀이
def calculate1(n1, n2, o):
    operators = {
        "add": (lambda x, y: x + y),
        "subtract": (lambda x, y: x - y),
        "multiply": (lambda x, y: x * y),
    }

    return "{:b}".format(operators[o](int(n1, 2), int(n2, 2)))