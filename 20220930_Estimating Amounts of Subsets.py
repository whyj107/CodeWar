# Estimating Amounts of Subsets
# https://www.codewars.com/kata/584703d76f6cf6ffc6000275/train/python

# 나의 풀이
# 조합 : nCr = n!/(r!(n-r)!)
from math import factorial
def est_subsets(arr):
    arr = list(set(arr))
    l_arr = len(arr)
    n = factorial(l_arr)
    result = 0
    for i in range(1, l_arr+1):
        result += n//(factorial(i)*factorial(l_arr-i))
    return result

# 다른 사람의 풀이
def est_subsets1(arr):
    return 2**len(set(arr)) - 1

print(est_subsets([1, 2, 3, 4]), 15)
print(est_subsets(['a', 'b', 'c', 'd', 'd']), 15)

arr = [2, 3, 4, 5, 5, 6, 6, 7, 8, 8]
print(est_subsets(arr), 127)

arr = ['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm']
print(est_subsets(arr), 511)

arr = [1] * 8
print(est_subsets(arr), 1)

arr = []
print(est_subsets(arr), 0)