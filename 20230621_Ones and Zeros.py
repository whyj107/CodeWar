# Ones and Zeros
# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

# 나의 풀이
def binary_array_to_number(arr):
    return int(''.join(str(_) for _ in arr), 2)

def solve(arr):
    result = 0
    for idx, a in enumerate(arr[::-1]):
        result += a*pow(2, idx)
    return result

# 다른 사람의 풀이
def binary_array_to_number2(arr):
    return int("".join(map(str, arr)), 2)

print(solve([0, 0, 0, 1]), 1)
print(binary_array_to_number([0, 0, 0, 1]), 1)
print(binary_array_to_number([0, 0, 1, 0]), 2)
print(binary_array_to_number([1, 1, 1, 1]), 15)
print(binary_array_to_number([0, 1, 1, 0]), 6)