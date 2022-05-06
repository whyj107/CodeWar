# Jaden Casing Strings
# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

# 나의 풀이
def to_jaden_case(string):
    return ' '.join([s.capitalize() for s in string.split()])

# 다른 사람의 풀이
import string
def toJadenCase1(NonJadenStrings):
    return string.capwords(NonJadenStrings)

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")