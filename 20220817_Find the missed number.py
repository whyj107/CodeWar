# Find the missed number
# https://www.codewars.com/kata/5a1d86dbba2a142e040000ee/train/python

# 풀이
from collections import Counter
from itertools import permutations

def find_number(start, stop, s):
    miss = Counter(''.join(map(str, range(start, stop+1)))) - Counter(s)
    intValues = {int(v) for v in map(''.join, permutations(''.join(c*n for c,n in miss.items()))) if v and v[0] != '0'}
    return [ v for v in intValues if start <= v <= stop ]

# 다른 사람의 풀이
def find_number1(start, stop, string):
    code = Counter(c for n in range(start, stop + 1) for c in str(n)) - Counter(string)
    return [n for n in range(start, stop + 1) if Counter(str(n)) == code]

string = "1116122137143151617181920849510"
print(find_number(1, 21, string), [12, 21])
