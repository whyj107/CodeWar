# Balanced Number (Special Numbers Series #1 )
# https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

# 나의 풀이
def balanced_num(number):
    n = list(map(int, str(number)))
    middle = len(n)//2 + 1
    return 'Balanced' if sum(n[middle:]) == sum(n[::-1][middle:]) or len(n) < 3 else 'Not Balanced'

# 다른 사람의 풀이
def balancedNum1(n):
    s = str(n)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"

# print(balanced_num(7), "Balanced")
print(balanced_num(959), "Balanced")
# print(balanced_num(13), "Balanced")
print(balanced_num(432), "Not Balanced")
print(balanced_num(424), "Balanced")

print(balanced_num(1024), "Not Balanced")
print(balanced_num(66545), "Not Balanced")
print(balanced_num(295591), "Not Balanced")
print(balanced_num(1230987), "Not Balanced")
print(balanced_num(56239814), "Balanced")
