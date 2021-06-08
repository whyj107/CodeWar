# Kaprekar Split
# https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7/train/python

# 나의 풀이
def kaprekar_split(n):
    step1 = str(n**2)
    if len(step1) < 2: return 0
    for idx in range(1, len(step1)):
        if int(step1[:idx]) + int(step1[idx:]) == n:
            return idx
    return -1

# 다른 사람의 풀이
def kaprekar_split1(n):
    s = str(n ** 2)
    for i in range(len(s)):
        if int(s[:i] or 0) + int(s[i:] or 0) == n:
            return i
    return -1

print(kaprekar_split(1), 0)
print(kaprekar_split(9), 1)
print(kaprekar_split(45), 2)
print(kaprekar_split(2223), 3)
print(kaprekar_split(5050), 4)
print(kaprekar_split(5051), -1)
print(kaprekar_split(9999999999), 10)