# Boxlines
# https://www.codewars.com/kata/6129095b201d6b000e5a33f0/train/python

# 나의 풀이
def f(x, y, z):
    return (x+1)*(y+1)*z + (x+1)*y*(z+1) + x*(y+1)*(z+1)

# 다른 사람의 풀이
def f1(x,y,z):
    return x+(x+2)*y*z + y+(y+2)*x*z + z+(z+2)*x*y

print(f(2, 1, 1), 20)
print(f(1, 2, 3), 46)
print(f(2, 2, 2), 54)