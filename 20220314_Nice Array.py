# Nice Array
# https://www.codewars.com/kata/59b844528bcb7735560000a0/train/python

# 나의 풀이
def is_nice(arr):
    if arr == []: return False
    return sum(1 for a in arr if a-1 in arr or a+1 in arr) == len(arr)

# 다른 사람의 풀이
def is_nice1(arr):
    s = set(arr)
    return bool(arr) and all( n+1 in s or n-1 in s for n in s)

def is_nice2(arr):
    return all(x+1 in arr or x-1 in arr for x in arr) and len(arr)>0

print(is_nice([2, 10, 9, 3]), True)
print(is_nice([3, 4, 5, 7]), False)