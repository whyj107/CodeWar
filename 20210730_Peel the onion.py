# Peel the onion
# https://www.codewars.com/kata/60fa9511fb42620019966b35/train/python

# 나의 풀이
def peel_the_onion(s, d):
    tmp = pow(s, d)
    print(tmp)
    return [tmp]

sample_test_cases = [
#        s  d     result
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

for _, test_cases in sample_test_cases:
    for s, d, ex in test_cases:
        print(peel_the_onion(s, d), ex)