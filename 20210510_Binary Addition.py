# Binary Addition
# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

# 나의 풀이
def add_binary(a, b):
    return format(a+b, 'b')

# 다른 사람의 풀이
def add_binary1(a, b):
    return bin(a+b)[2:]

print(add_binary(1,1),"10")
print(add_binary(0,1),"1")
print(add_binary(1,0),"1")
print(add_binary(2,2),"100")
print(add_binary(51,12),"111111")