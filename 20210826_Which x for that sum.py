# Which x for that sum?
# https://www.codewars.com/kata/5b1cd19fcd206af728000056/train/python

# 나의 풀이
def solve(m):
    # U(n, x) = x + 2x**2 + 3x**3 + ... + nx**n
    # solve(2.0) => U(무한, 0.5)
    # m = x/((1-x)**2)
    # 적분해야할 것 같은데 나중에 다시 풀어보자
    result = 0
    for i in range(1, m+1):
        result += (i*0.6096**i)
    return result

print(solve(100))