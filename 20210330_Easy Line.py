# Easy Line
# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

# 이항계수를 이용해서 푸는 문제
from math import factorial
def easyline(n):
    return factorial(2*n)//(factorial(n)**2)

def easyline1(n):
    return easyline(n-1)*(4*n-2)//n if n else 1

print(easyline(7), 3432)
print(easyline(13), 10400600)
print(easyline(17), 2333606220)
print(easyline(19), 35345263800)