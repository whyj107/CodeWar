# Playing on a chessboard
# https://www.codewars.com/kata/55ab4f980f2d576c070000f4/train/python

# 나의 풀이 : 시간 초과
from fractions import Fraction
def game0(n):
    result = Fraction(0)
    for i in range(1, n+1):
        for j in range(1, n+1):
            result += Fraction(j, j+i)
    return [result.numerator, result.denominator] if result.denominator != 1 else [result.numerator]

def game(n):
    tmp1, tmp2 = 0, 0
    for i in range(0, n):
        tmp1 += tmp2
        tmp2 += 0.5
    result = Fraction(tmp1*2+tmp2)
    return [result.numerator, result.denominator] if result.denominator != 1 else [result.numerator]

# 다른 사람의 풀이
'''
        n    t(i)     n-1  (n + i + 1) * (n - i)
s(n) =  Σ   -----  +   Σ   ---------------------
       i=1  i + 1     i=1     2 * (n + i + 1)

        n    i      n-1   n - i
     =  Σ   ---  +   Σ    -----
       i=1   2      i=1     2

        n    i      n-1    i
     =  Σ   ---  +   Σ    ---
       i=1   2      i=1    2

         n      n-1
     =  ---  +   Σ   i
         2      i=1

         n      n * (n - 1)
     =  ---  +  -----------
         2          2

     =  n^2 / 2
'''
def game1(n):
    return [n**2, 2] if n % 2 else [n**2 // 2]

print(game(0), [0])
print(game(1), [1, 2])
print(game(8), [32])
