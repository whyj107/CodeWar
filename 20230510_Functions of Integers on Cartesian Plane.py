# Functions of Integers on Cartesian Plane
# https://www.codewars.com/kata/559e3224324a2b6e66000046/train/python

# 나의 풀이
def sumin(n):
    return sum([i*(1+i)//2 + i*(n-i) for i in range(1, n+1)])

def sumax(n):
    return sum([(i+n)*(n-i+1)//2 + (i-1)*i for i in range(1, n+1)])

def sumsum(n):
    return sum([(2*i+n-1)*n//2 for i in range(2, n+2)])

# 다른 사람의 풀이
"""
def sumin(n):
    return n * (n + 1) * (2 * n + 1) // 6
    
def sumax(n):
    return n * (n + 1) * (4 * n - 1) // 6
    
def sumsum(n):
    return n * n * (n + 1)
"""

print(sumin(5), 55)
print(sumax(8), 372)
print(sumsum(8), 576)
print(sumin(15), 1240)
