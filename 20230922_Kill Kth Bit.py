# Simple Fun #8: Kill K-th Bit
# https://www.codewars.com/kata/58844f1a76933b1cd0000023/train/python

# 나의 풀이
def kill_kth_bit(n, k):
    b_n = bin(n)[2:]
    if len(b_n) < k: return n
    tmp = list(map(str, b_n[::-1]))
    tmp[k-1] = '0'
    r = ''.join(tmp[::-1])
    return int(r, 2)

# 다른 사람의 풀이
def f(n, k):
    return n & ~(1<<k-1)

print(kill_kth_bit(37, 3), 33)
print(kill_kth_bit(37, 4), 37)
print(kill_kth_bit(0, 4), 0)
