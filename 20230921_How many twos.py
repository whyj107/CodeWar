# How many twos?
# https://www.codewars.com/kata/56aed5db9d5cb55de000001c/train/python

# 풀이
def two_count(n):
    res = 0
    while not n & 1:
        res += 1
        n >>= 1
    return res

def two_count1(n):
  return bin(n)[::-1].index('1')

print(two_count(1), 0)
print(two_count(2), 1)
print(two_count(7), 0)
print(two_count(24), 3)
print(two_count(256), 8)
print(two_count(17280), 7)
print(two_count(84934656), 20)
print(two_count(222222222222), 1)
print(two_count(7777777777777777), 0)
print(two_count(482848428248882482), 1)