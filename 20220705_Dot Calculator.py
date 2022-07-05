# Dot Calculator
# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/python

# My Solution
def calculator(txt):
    oper = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, '//': lambda x, y: x//y}
    txt = txt.split()
    return '.' * oper[txt[1]](len(txt[0]), len(txt[2]))

def calculator1(txt):
    a, op, b = txt.split()
    a, b = len(a), len(b)
    return '.' * eval(f'{a} {op} {b}')

print(calculator("..... + ..............."), "....................")
print(calculator("..... - ..."), "..")
print(calculator("..... - ."), "....")
print(calculator("..... * ..."), "...............")
print(calculator("..... * .."), "..........")
print(calculator("..... // .."), "..")
print(calculator("..... // ."), ".....")
print(calculator(". // .."), "")
print(calculator(". - ."), "")
