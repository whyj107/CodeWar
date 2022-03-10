# Function Composition
# 6 kyu
# https://www.codewars.com/kata/5421c6a2dda52688f6000af8/train/python

# 다른 사람의 풀이
compose = lambda f, g: lambda *x: f(g(*x))

def compose(f, g):
    return lambda *x: f(g(*x))

add1 = lambda a: a+1
this = lambda a: a

print(compose(add1, this)(0) == 1)