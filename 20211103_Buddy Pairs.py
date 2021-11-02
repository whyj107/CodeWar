# Buddy Pairs
# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python

# 나의 풀이
def buddy(start, limit):
    for i in range(start, limit+1):
        a = sum(GetDivisor(i)) - i - 1
        b = sum(GetDivisor(a)) - a - 1
        if i == b and i < a:
            return [i, a]
    return "Nothing"

def GetDivisor(n):
    d = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            d.append(i)
            if i != (n//i):
                d.append(n//i)
    return d


print(buddy(48, 50), [48, 75])
print(buddy(2177, 4357), "Nothing")
print(buddy(57345, 90061), [62744, 75495])
print(buddy(1071625, 1103735), [1081184, 1331967])