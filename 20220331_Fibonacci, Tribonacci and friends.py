# Fibonacci, Tribonacci and friends
# https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python

# 나의 풀이
def Xbonacci(signature, n):
    sig = len(signature)
    result = signature + [0]*(n-sig)
    for i in range(sig, n):
        result[i] = sum(result[i-sig:i])
    return result[:n]

# 다른 사람의 풀이
def Xbonacci1(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output

print(Xbonacci([0, 1], 10),
               [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(Xbonacci([1, 1], 10),
               [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
print(Xbonacci([0, 0, 0, 0, 1], 10),
               [0, 0, 0, 0, 1, 1, 2, 4, 8, 16])
print(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10),
               [1, 0, 0, 0, 0, 0, 1, 2, 3, 6])
print(Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20),
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256])
