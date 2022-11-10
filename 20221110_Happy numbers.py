# Happy numbers
# https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e/train/python

# 나의 풀이
def is_happy(n):
    tmp = []
    while 1 != n:
        n = sum([int(i)**2 for i in str(n)])
        if n in tmp: return False
        tmp.append(n)
    return True

# 다른 사람의 풀이
def is_happy1(n):
    seen = set()
    while n!=1:
        n = sum(int(d)**2 for d in str(n))
        if n not in seen: seen.add(n)
        else:             return False
    return True

def is_happy2(n):
    while n > 4:
        n = sum(int(d)**2 for d in str(n))
    return n == 1

print(is_happy(1), True)
print(is_happy(7), True)
print(is_happy(901), True)
print(is_happy(16), False)
print(is_happy(37), False)

"""
for i in range(1, 5001):
    print(is_happy(i))
"""
