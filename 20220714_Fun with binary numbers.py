# Fun with binary numbers
# https://www.codewars.com/kata/5ce04eadd103f4001edd8986/train/python

# 나의 풀이
def solution(n, b):
    result = []
    if b == 0: return result
    cnt = 0
    while 2**cnt != b:
        cnt += 1
    for i in range(1, pow(2, n)):
        if len(format(i, 'b')) < cnt+1: continue
        if format(i, 'b')[::-1][cnt] == '1':
            result.append(i)
    return result

# 다른 사람의 풀이
def solution1(n,b):
    return [x for x in range(1<<n) if x&b]

print(solution(4, 2) == [2, 3, 6, 7, 10, 11, 14, 15])
print(solution(6, 8) == [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63])
print(solution(5, 32) == [])
print(solution(6, 0) == [])
print(solution(0, 1) == [])