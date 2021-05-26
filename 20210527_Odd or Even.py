# Odd or Even?
# https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

# 나의 풀이
def odd_or_even(arr):
    return "odd" if sum(arr) % 2 != 0 else "even"

print(odd_or_even([0, 1, 2]), "odd")
print(odd_or_even([0, 1, 3]), "even")
print(odd_or_even([1023, 1, 2]), "even")