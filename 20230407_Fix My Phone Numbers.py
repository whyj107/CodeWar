# Fix My Phone Numbers!
# https://www.codewars.com/kata/596343a24489a8b2a00000a2/train/python

# 나의 풀이
def is_it_a_num(s: str) -> str:
    num = ''.join(i for i in s if i.isnumeric())
    return num if len(num)==11 and num[0]=='0' else 'Not a phone number'

# 다른 사람의 풀이
from functools import partial
from re import compile
REGEX = partial(compile(r"\D+").sub, "")
def is_it_a_num1(s: str) -> str:
    res = REGEX(s)
    if len(res) == 11 and res[0] == "0":
        return res
    return "Not a phone number"

print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
print(is_it_a_num("sjfniebienvr12312312312ehfWh"), "Not a phone number")
print(is_it_a_num("0192387415456"), "Not a phone number")
print(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
print(is_it_a_num("stop calling me no I have never been in an accident"), "Not a phone number")