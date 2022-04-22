# Odd-heavy Array
# https://www.codewars.com/kata/59c7e477dcc40500f50005c7/train/python

# 나의 풀이
def is_odd_heavy(arr):
    odd = [a for a in arr if a%2!=0]
    even = max([a for a in arr if a%2==0]+[-100])
    return False if odd == [] else min(odd)>even

# 다른 사람의 풀이
def isOddHeavy1(arr):
    maxEven = max(filter(lambda n: n%2 == 0, arr), default=float("-inf"))
    minOdd  = min(filter(lambda n: n%2 == 1, arr), default=float("-inf"))
    return maxEven < minOdd