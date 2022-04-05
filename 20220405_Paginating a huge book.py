# Paginating a huge book
# https://www.codewars.com/kata/55905b7597175ffc1a00005a/train/python

# How many pages in a book? 이라는 문제와 비슷하다
# https://www.codewars.com/kata/622de76d28bf330057cd6af8/train/python

# 나의 풀이
# 시간 초과
def page_digits0(pages):
    return len(''.join([str(i) for i in range(1, pages+1)]))

# 정답
from decimal import Decimal
def page_digits(pages):
    cnt = len(str(pages))
    tmp = 0 if cnt-1 == 0 else '9'*(cnt-1)
    res = 0
    for i in range(cnt):
        res += Decimal(9 * i * 10**(i-1))
    return res + (pages - int(tmp)) * cnt

# 다른 사람의 풀이
def page_digits1(pages):
    k, i = 0, 1
    while i <= pages:
        k += pages - i + 1
        i *= 10
    return k

print(page_digits(4), 4)
print(page_digits(12), 15)
print(page_digits(100), 192)
print(page_digits(400000000000000000), 7088888888888888907)