# Count characters in your string
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

# 나의 풀이
def count(string):
    result = {}
    for s in string:
        result.setdefault(s, 0)
        result[s] += 1
    return

# 다른 사람의 풀이
from collections import Counter
def count1(string):
    return Counter(string)

print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})