# Last digit of a large number
# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

# 나의 풀이
def last_digit(n1, n2):
    if n2 == 0: return 1
    tmp = {1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5],
           6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1], 0: [0]}
    n = tmp[n1 % 10]
    tmp = n2 % len(n)-1
    return n[tmp]

# 다른 사람의 풀이
def last_digit1(n1, n2):
    return pow(n1, n2, 10)

def last_digit2(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10

print(last_digit(4, 1), 4)
print(last_digit(4, 2), 6)
print(last_digit(9, 7), 9)
print(last_digit(10, 10 ** 10), 0)
print(last_digit(2 ** 200, 2 ** 300), 6)
print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)