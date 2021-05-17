# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

# 나의 풀이
def printer_error(s):
    return f'{sum([1 for i in s if ord(i) > 109])}/{len(s)}'

# 다른 사람의 풀이
from re import sub
def printer_error1(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s), "3/56")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s), "6/60")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
print(printer_error(s), "11/65")