# Functional Addition
# https://www.codewars.com/kata/538835ae443aae6e03000547/train/python

# 나의 풀이
def add(n):
    return lambda x: n+x

def add1(n):
    def adder(x):
        return x + n
    return adder

add_one = add(1)
print(add_one(3), 4)

add_three = add(3)
print(add_three(3), 6)