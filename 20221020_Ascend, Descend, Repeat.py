# Ascend, Descend, Repeat?
# https://www.codewars.com/kata/62ca07aaedc75c88fb95ee2f/train/python

# 나의 풀이
def ascend_descend(length, minimum, maximum):
    if minimum == maximum: return str(minimum)*length
    result = [str(i) for i in range(minimum, maximum, 1)] + [str(i) for i in range(maximum, minimum, -1)]
    result = ''.join(result) * length
    return result[:length]

# 다른 사람의 풀이
from math import ceil
def ascend_descend1(size,s,e):
    lst = [*range(s,e+1)]
    lst += lst[-2:0:-1]
    s = ''.join(map(str,lst))
    return s and (s * ceil(size/len(s)))[:size]

print(ascend_descend(5, 1, 3), "12321")
print(ascend_descend(14, 0, 2), "01210121012101")
print(ascend_descend(11, 5, 9), "56789876567")