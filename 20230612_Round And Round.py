# Simple Fun #296: Round And Round
# https://www.codewars.com/kata/591e8c715b1d254f9e00005e/train/python

# 나의 풀이
def round_and_round(n, a, b):
    return (a+b)%n or n

test_cases = [
    # n, a, b, result
    (6, 2, -5, 3), (5, 1, 3, 4), (3, 2, 7, 3),
    (100, 1, -1, 100), (100, 54, 100, 54), (97, 37, -92, 42),
    (99, 41, 0, 41), (35, 34, 1, 35), (3, 2, -100, 1),
    (1, 1, -100, 1), (100, 1, -10000, 1), (333, 222, 111, 333),
]


for n, a, b, expected in test_cases:
    print(round_and_round(n, a, b), expected, f'round_and_round({n}, {a}, {b})')