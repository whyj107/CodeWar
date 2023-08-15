# Array element parity
# https://www.codewars.com/kata/5a092d9e46d843b9db000064/train/python

# 나의 풀이
def solve(arr):
    arr = list(set(arr))
    return sum(arr)

sample_test_cases = [
    ([1, -1, 2, -2, 3],                 3),
    ([-3, 1, 2, 3, -1, -4, -2],        -4),
    ([1, -1, 2, -2, 3, 3],              3),
    ([-9, -105, -9, -9, -9, -9, 105],  -9),
    ([-110, 110, -38, -38, -62, 62, -38, -38, -38],  -38),
]

for arr, expected in sample_test_cases:
    msg = f'solve({arr})'
    print(solve(arr), expected, msg)