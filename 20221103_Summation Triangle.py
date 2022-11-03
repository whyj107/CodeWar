# Summation Triangle #2
# https://www.codewars.com/kata/63579823d25aad000ecfad9f/train/python

# 나의 풀이
import numpy as np
def get_sum0(n):
    a = np.arange(1, n+2)
    a = a*(2*a+(a-1)*2)//2*pow(-1, 2*a+(a-1))
    return a.sum()

# 다른 사람의 풀이
def get_sum(n):
    '''
    Expansion of x*(1 + 3*x)/((1 + x)*(1 - x)^3).
    a(n) = n^2 + n - 1 - floor((n-1)/2)

    0, 1, 5, 10, 18, 27, 39, 52, 68, 85, 105, 126,
    150, 175, 203, 232, 264, 297, 333, 370, 410, 451,
    495, 540, 588, 637, 689, 742, 798, 855, 915, 976,
    1040, 1105, 1173, 1242, 1314, 1387, 1463, 1540,
    1620, 1701, 1785, 1870, 1958, 2047, 2139, 2232,
    2328, 2425
    '''
    n += 1
    return (-1)**(n+1) * (n**2 + n - 1 - (n - 1) // 2)

"""
print(get_sum(0), 1)
print(get_sum(1), -5)
print(get_sum(2), 10)
print(get_sum(3), -18)
"""

for i in range(10):
    print(f'{i}: {get_sum(i)}')
    print('-------------------')
