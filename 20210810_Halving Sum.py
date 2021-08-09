# Halving Sum
# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

# 나의 풀이
def halving_sum(n):
    result = []
    idx = 1
    while n//idx > 1:
        result.append(n//idx)
        idx *= 2
    return sum(result)+1

# 다른 사람의 풀이
# 비트 이용
def halving_sum1(n):
    s=0
    while n:
        s+=n ; n>>=1
    return s

# 재귀
def halving_sum2(n):
    if n == 1:
        return 1
    else:
        return n + halving_sum(n//2)

print(halving_sum(25), 47)
print(halving_sum(127), 247)