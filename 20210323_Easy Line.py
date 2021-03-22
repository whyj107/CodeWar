# Easy Line
# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

# 수학적 내용 좀 더 공부해보기

# 다른 사람의 풀이
from math import factorial
def easyline1(n):
    return factorial(2*n)/(factorial(n)**2)

def easyline2(n):
    return easyline2(n-1)*(4*n-2)//n if n else 1

print(easyline1(7), 3432)
print(easyline2(13), 10400600)
print(easyline2(17), 2333606220)
print(easyline2(19), 35345263800)