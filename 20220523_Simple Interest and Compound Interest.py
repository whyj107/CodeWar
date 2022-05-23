# Simple Interest and Compound Interest
# https://www.codewars.com/kata/59cd0535328801336e000649/train/python

# 나의 풀이
def interest0(p, r, n):
    # 단순 이자
    x = p + p * r * n
    # 복리 이자
    for _ in range(n):
        p = p + p * r
    return [round(x), round(p)]

def interest(p, r, n):
    return [round(p + p * r * n), round(p*(1+r)**n)]



print(interest(100, 0.1, 1), [110, 110])
print(interest(100, 0.1, 2), [120, 121])