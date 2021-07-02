# FIXME: Replace all dots
# https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python

# 나의 풀이
import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)

def replace_dots1(string):
    return string.replace('.', '-')

print(replace_dots(""), "")
print(replace_dots("no dots"), "no dots")
print(replace_dots("one.two.three"), "one-two-three")
print(replace_dots("........"), "--------")