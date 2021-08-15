# Multiples!
# https://www.codewars.com/kata/55a8a36703fe4c45ed00005b/train/python

# 나의 풀이
def multiple(x):
    result = ''
    if x % 3 == 0:
        result += 'Bang'
    if x % 5 == 0:
        result += 'Boom'
    elif x%3 != 0 and x%5 != 0:
        result = "Miss"
    return result

# 다른 사람의 풀이
def multiple1(x):
    return 'Bang' * (x % 3 == 0) + 'Boom' * (x % 5 == 0) or 'Miss'

print(multiple(30),  "BangBoom")
print(multiple(3), "Bang")
print(multiple(98), "Miss")
print(multiple(65), "Boom")
print(multiple(23), "Miss")
print(multiple(15), "BangBoom")