# Simple Fun #154: Zero And One
# https://www.codewars.com/kata/58ad09d6154165a1c80000d1/train/python

# 나의 풀이
def zero_and_one(s):
    result = []
    for i in s:
        if not result:
            result.append(i)
        elif result[-1] != i and result[-1] != ' ':
            result[-1] = ' '
        else:
            result.append(i)
    return result.count('1') + result.count('0')

# 다른 사람의 풀이
import re
def zero_and_one1(s):
    return len(re.sub("01|10", "", s))

def zero_and_one2(s):
    return len(s.replace('01', '').replace('10', ''))

print(zero_and_one("01010"), 1)
print(zero_and_one("11101111"), 6)
print(zero_and_one("01"), 0)
print(zero_and_one("10"), 0)
print(zero_and_one("110110"), 2)
print(zero_and_one("110100"), 2)
print(zero_and_one("1101101010110000101010011001100000000101101001000011010110"), 16)