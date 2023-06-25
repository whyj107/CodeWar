# Summing a numbmer's digits
# https://www.codewars.com/kata/52f3149496de55aded000410/train/python

# 나의 풀이
def sum_digits(number):
    return sum([int(n) for n in str(number) if n.isnumeric()])

print(sum_digits(10), 1)
print(sum_digits(99), 18)
print(sum_digits(-32), 5)