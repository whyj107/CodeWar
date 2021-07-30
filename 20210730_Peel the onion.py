# Peel the onion
# https://www.codewars.com/kata/60fa9511fb42620019966b35/train/python

# 풀이
def peel_the_onion1(s, d):
    return [i**d - (i - 2) ** d if i > 1 else 1 for i in range(s, 0, -2)]

def peel_the_onion(s, d):
    i = [2, 1][s % 2]
    lst = []
    while i <= s:
        lst.append(i ** d - sum(lst))
        i += 2
    return lst[::-1]

sample_test_cases = [
    (1, [
        (1, 1,    [1]),
        (2, 1,    [2]),
        (3, 1,    [2, 1]),
        (4, 1,    [2, 2]),
        (5, 1,    [2, 2, 1]),
    ]),
    (2, [
        (1, 2,    [1]),
        (2, 2,    [4]),
        (3, 2,    [8, 1]),
        (4, 2,    [12, 4]),
        (5, 2,    [16, 8, 1]),
    ]),
    (3, [
        (1, 3,    [1]),
        (2, 3,    [8]),
        (3, 3,    [26, 1]),
        (4, 3,    [56, 8]),
        (5, 3,    [98, 26, 1]),
    ]),
    (4, [
        (1, 4,    [1]),
        (2, 4,    [16]),
        (3, 4,    [80, 1]),
        (4, 4,    [240, 16]),
        (5, 4,    [544, 80, 1]),
    ]),
]

for d, test_cases in sample_test_cases:
        for s, d, expected in test_cases:
            print(peel_the_onion(s, d), expected)