# Which x for that sum?
# https://www.codewars.com/kata/5b1cd19fcd206af728000056/train/python

# 나의 풀이
def solve(m):
    # m = x + 2x**2 + 3x**3 + ... + nx**n
    # m = x/(x-1)**0.5
    # mx**2 + 2(-m-0.5)x + m = 0
    # 근의 공식 사용 / use quadratic formula
    # x range 0<x<1
    return 1+0.5/m - ((m+0.25)**0.5)/m

print(solve(100))
