# Digitize
# https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python

# 나의 풀이
def digitize(n):
    return list(int(i) for i in str(n))

# 다른 사람의 풀이
def digitize1(n):
    return list(map(int, str(n)))

print(digitize(123), [1,2,3])
print(digitize(1), [1])
print(digitize(0), [0])
print(digitize(1230), [1, 2, 3, 0])
print(digitize(8675309), [8, 6, 7, 5, 3, 0, 9])