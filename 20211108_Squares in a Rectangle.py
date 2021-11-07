# Squares in a Rectangle
# https://www.codewars.com/kata/5a62da60d39ec5d947000093/train/python

# 다른 사람의 풀이
def findSquares(x, y):
    return sum((x-i) * (y-i) for i in range(y) )

def findSquares1(x,y):
    if x > y:
        x, y = y, x
    return x*(x+1)*(2*x+1)/6 + (y-x)*x*(x+1)/2

def findSquares2(x,y):
    squares = 0
    while y > 0:
        squares = squares + x*y
        x = x-1
        y = y-1
    return squares

print(findSquares(3, 2), 8)
print(findSquares(4, 3), 20)
print(findSquares(11, 4), 100)
