# A Rule of Divisibility by 13
# https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python

# 나의 풀이
def thirt(n):
    pre = 0
    while pre != n:
        pre = n
        n = sum([int(i)*(pow(10, idx) % 13)for idx, i in enumerate(str(n)[::-1])])
    return n

# 다른 사람의 풀이
array = [1, 10, 9, 12, 3, 4]
def thirt1(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)


import itertools as it
def thirt2(n):
    if n < 100: return n
    pattern = it.cycle([1, 10, 9, 12, 3, 4])
    return thirt(sum(d * n for d, n in zip(map(int, str(n)[::-1]), pattern)))

print(thirt(8529), 79)
print(thirt(85299258), 31)
print(thirt(5634), 57)
print(thirt(1111111111), 71)
print(thirt(987654321), 30)
