# Cubes in the box
# https://www.codewars.com/kata/61432694beeca7000f37bb57/train/python

# 나의 풀이
def f(x, y, z):
    return sum((x-i)*(y-i)*(z-i) for i in range(min(x, y, z)))

sample_test_cases = [
    ((2, 2, 3), 14),
    ((3, 4, 2), 30),
    ((3, 3, 3), 36)
]

for (x, y, z), expected in sample_test_cases:
    print(f(x, y, z), expected)