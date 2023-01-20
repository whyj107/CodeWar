# Price of Mangoes
# https://www.codewars.com/kata/57a77726bb9944d000000b06/train/python

# 나의 풀이
def mango(quantity, price):
    a, b = divmod(quantity, 3)
    return (a*2+b)*price

# 다른 사람의 풀이
def mango1(quantity, price):
    return (quantity - quantity // 3) * price

print(mango(3, 3), 6)
print(mango(9, 5), 30)