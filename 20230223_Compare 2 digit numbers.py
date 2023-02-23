# Compare 2 digit numbers
# https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/train/python

# 나의 풀이
def compare(a, b):
    a = set(map(int, str(a)))
    b = set(map(int, str(b)))
    return f'{len(a&b)/max(len(a),len(b))*100:.0f}%'

# 다른 사람의 풀이
def compare1(a, b):
    sa, sb = set(str(a)), set(str(b))
    c, d = sa & sb, sa | sb
    return "100%" if sa == sb else f"{len(c)*50}%"

tests = [
    (10, 11, "50%"),
    (33, 33, "100%"),
    (45, 45, "100%"),
    (29, 92, "100%"),
    (14, 24, "50%"),
    (56, 57, "50%"),
    (38, 84, "50%"),
    (10, 22, "0%"),
    (11, 44, "0%"),
    (98, 70, "0%"),
    (66, 16, "50%"),
    (98, 88, "50%"),
    (78, 58, "50%"),
    (47, 56, "0%")
]

for a, b, expected in tests:
    print(compare(a, b), expected, f"a = {a}, b = {b}")
