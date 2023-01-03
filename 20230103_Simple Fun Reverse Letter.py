# Simple Fun #176: Reverse Letter
# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/python

# 나의 풀이
def reverse_letter(string):
    return ''.join([s for s in string[::-1] if s.isalpha()])

# 다른 사람의 풀이
def reverse_letter1(string):
    return ''.join(filter(str.isalpha, reversed(string)))

import re
def reverse_letter2(string):
    return re.sub("[^a-zA-Z]","",string)[::-1]

print(reverse_letter("krishan"), "nahsirk")
print(reverse_letter("ultr53o?n"), "nortlu")
print(reverse_letter("ab23c"), "cba")
print(reverse_letter("krish21an"), "nahsirk")