# Collatz Conjecture Length
# https://www.codewars.com/kata/54fb963d3fe32351f2000102/train/python

# 나의 풀이
def collatz(n):
    result = [n]
    while n != 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        result.append(n)
    return len(result)

# 다른 사람의 풀이
def collatz1(n, c=1):
    return collatz(n / 2, c + 1) if n % 2 == 0 else (collatz(n * 3 + 1, c + 1) if n != 1 else c)

def collatz2(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n / 2) + 1
    else:
        return collatz(3 * n + 1) + 1

print(collatz(20), 8)
print(collatz(15), 18)