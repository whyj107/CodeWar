# [Code Golf] Reversed Upper Index
# https://www.codewars.com/kata/62f8d0ac2b7cd50029dd834c/train/python

# 풀이
# ~x == -x-1
# -~x == x+1
# 소문자가 대문자보다 크다
f=lambda s:s[-1]>"Z"and-~f(s[:-1])

f1=lambda x:1+f1(x[:-1])if x[-1]>'Z'else 0
f2=lambda s:[i<='Z'for i in s[::-1]].index(1)

print(f("HelloWorld"), 4)
print(f("Codewars"), 7)
print(f("X"), 0)
print(f("findX"), 0)