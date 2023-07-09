# Last non-zero digit of factorial
# https://www.codewars.com/kata/5f79b90c5acfd3003364a337/train/python

# 나의 풀이
def last_digit(n):
    tmp = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]
    if n < 10: return tmp[n]

    if ((n // 10) % 10) % 2 == 0:
        return (6 * last_digit(n // 5) * tmp[n % 10]) % 10
    else:
        return (4 * last_digit(n // 5) * tmp[n % 10]) % 10

print(last_digit(3), 6)
print(last_digit(99), 4)
print(last_digit(12), 6)
print(last_digit(387), 2)
print(last_digit(1673), 4)
print(last_digit(10000), 8)