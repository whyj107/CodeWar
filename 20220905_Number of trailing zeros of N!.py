# Number of trailing zeros of N!
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

# 나의 풀이
from math import factorial
# 시간 초과....
def zeros0(n):
    cnt = {2: 0, 5: 0}
    for i in range(2, n+1):
        tmp_2, tmp_5 = i, i
        while tmp_2 % 2 == 0:
            cnt[2] += 1
            tmp_2 //= 2

        while tmp_5 % 5 == 0:
            cnt[5] += 1
            tmp_5 //= 5
    return min(cnt.values())

from math import factorial
def zeros1(n):
    cnt = 0
    for i in str(factorial(n))[::-1]:
        if i == '0':
            cnt += 1
        else:
            break
    return cnt

# 5의 갯수로 계산하기 -> 2는 넉넉할 것 같아서
def zeros(n):
    cnt = 0
    tmp = 1
    while n >= pow(5, tmp):
        cnt += (n//(pow(5, tmp)))
        tmp += 1
    return cnt

# 다른 사람의 풀이 : 재귀로 풀었다
def zeros_(n):
  x = n/5
  return x+zeros_(x) if x else 0

print(zeros(0), 0)
print(zeros(6), 1)
print(zeros(30), 7)