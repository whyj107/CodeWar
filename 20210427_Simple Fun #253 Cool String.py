# Simple Fun #253: Cool String
# https://www.codewars.com/kata/590fd3220f05b4f1ad00007c/train/python

# 나의 풀이
def cool_string(s):
    tmp = [i.islower() for i in s if i.isalpha()]
    if len(tmp) != len(s): return False
    for i in range(len(tmp)-1):
        if tmp[i] == tmp[i+1]: return False
    return True

# 다른 사람의 풀이
def cool_string1(s):
    return s.isalpha() and all(x.islower() != y.islower() for x, y in zip(s, s[1:]))

import re
def cool_string2(s):
    return re.match(r'^(?!.*[a-z]{2})(?!.*[A-Z]{2})[a-zA-Z]+$', s) is not None

def cool_string3(s):
    s = s[::2] + s[1::2].swapcase()
    return s.isalpha() and  s.isupper()^s.islower()

print(cool_string("aQwFdA"), True)
print(cool_string("aBC"), False)
print(cool_string("AaA"), True)
print(cool_string("q q"), False)
print(cool_string("wWw1"), False)
print(cool_string("2"), False)
print(cool_string("aAaAaAa"), True)
print(cool_string("    "), False)