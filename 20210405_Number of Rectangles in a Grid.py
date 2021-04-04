# Number of Rectangles in a Grid
# https://www.codewars.com/kata/556cebcf7c58da564a000045/train/python

# 다른 사람의 풀이
# 공식이 있는 모양이다. 외워두자.
def number_of_rectangles(m, n):
    return (m * m + m) * (n * n + n) / 4

def number_of_rectangles1(m, n):
    return n*m*(n+1)*(m+1)/4

def number_of_rectangles2(m, n):
    return sum(i*j for i in range(m + 1) for j in range(n + 1))

print(number_of_rectangles(4, 4), 100, "Should be 100")
print(number_of_rectangles(5, 5), 225, "Should be 225")