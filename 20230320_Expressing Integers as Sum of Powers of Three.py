# Expressing Integers as Sum of Powers of Three
# https://www.codewars.com/kata/6012457c0aa675001d4d560b/train/python

# 나의 풀이
def as_sum_of_powers_of_3(n):
    three = {0:'0', 1:'+', -1: '-', -2:'+-', 2:'-+'}
    tmp = []
    while abs(n) > 2:
        a, b = divmod(n, 3)
        if b == 2:
            tmp.append('-')
            a += 1
        else:
            tmp.append(three[b])
        n = a
    tmp.append(three[n])
    return ''.join(tmp)

# 다른 사람의 풀이
def as_sum_of_powers_of_3_2(n):
    if not n: return '0'
    r = ''
    while n != 0:
        k = n % 3
        r += '0+-'[k]
        if k == 2: k = -1
        n = (n - k) // 3
    return r

print(as_sum_of_powers_of_3(-0), "0")
print(as_sum_of_powers_of_3(3), "0+")
print(as_sum_of_powers_of_3(-4), "--")
print(as_sum_of_powers_of_3(8), "-0+")
print(as_sum_of_powers_of_3(-13), "---")
print(as_sum_of_powers_of_3(81), "0000+")
print(as_sum_of_powers_of_3(-360), "00----")
print(as_sum_of_powers_of_3(1066), "+++0+++")
print(as_sum_of_powers_of_3(-544))