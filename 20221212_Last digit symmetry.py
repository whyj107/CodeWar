# Last digit symmetry
# https://www.codewars.com/kata/59a9466f589d2af4c50001d8/train/python

# 나의 풀이
def solve(a, b):
    cnt = 0
    back = ['00', '01', '25', '76']
    primes = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47',
              '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    for n in range(max(a, 1176), b):
        n1 = str(n)
        if n1[-2:] in back:
            n2 = str(n ** 2)
            if n1[-2:] == n2[-2:]:
                if n1[:2] in primes and n2[:2] in primes:
                    cnt += 1
    return cnt

# 다른 사람의 풀이
ls = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
def solve1(a,b):
    i = a
    s = 0
    while i < b:
        if (i*i-i)%100==0 and str(i)[:2] in ls and str(i*i)[:2] in ls:
            s += 1
        i += 1
    return s

print(solve(2, 10))
print(solve(2, 1200), 1)
print(solve(1176, 1200), 1)
print(solve(1176, 2000), 1)
print(solve(2, 100000), 247)
print(solve(2, 1000000), 2549)
print(solve(100000, 1000000), 2302)
print(solve(2, 1000000), 2549)
