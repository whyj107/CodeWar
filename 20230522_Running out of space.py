# Running out of space
# https://www.codewars.com/kata/56576f82ab83ee8268000059/train/python

# 나의 풀이
def spacey(array):
    result = []
    tmp = ''
    for a in array:
        tmp += a
        result.append(tmp)
    return result

# 다른 사람의 풀이
from itertools import accumulate
def spacey1(a):
    return list(accumulate(a))

def spacey2(array):
    return [''.join(array[:i+1]) for i in range(len(array))]

print(spacey(['kevin', 'has','no','space']), [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
print(spacey(['this','cheese','has','no','holes']), ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes'])