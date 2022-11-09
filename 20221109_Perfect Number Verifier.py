# Perfect Number Verifier
# https://www.codewars.com/kata/56a28c30d7eb6acef700004d/train/python

# 나의 풀이
def is_perfect(n):
    return sum(divisor(n)) - n == n

# 약수 구하기
def divisor(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            result.append(n//i)
    return set(result)

print(is_perfect(1), False)
print(is_perfect(2), False)
print(is_perfect(6), True)
print(is_perfect(28), True)
print(is_perfect(120), False)
print(is_perfect(496), True)
print(is_perfect(1234), False)
print(is_perfect(2016), False)
print(is_perfect(8128), True)