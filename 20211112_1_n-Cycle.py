# 1/n-Cycle
# https://www.codewars.com/kata/5a057ec846d843c81a0000ad/train/python

# 다른 사람의 풀이
def cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    k = 1
    while pow(10, k, n) != 1:
        k += 1
    return k

def cycle1(n) :
    if n % 2 and n % 5:
        for i in range(1, n):
            if pow(10, i, n) == 1:
                return i
    return -1

print(cycle(33), 2)
print(cycle(18118), -1)
print(cycle(69), 22)
print(cycle(197), 98)
print(cycle(65), -1)


