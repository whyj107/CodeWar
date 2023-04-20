# Quadrants
# https://www.codewars.com/kata/643af0fa9fa6c406b47c5399/train/python

# 나의 풀이
def quadrant(x, y):
    return 1 if x>0 and y>0 else (2 if x<0 and y>0 else (3 if x<0 and y<0 else 4))


# 다른 사람의 풀이
quadrant1 = lambda x, y: ((1,2),(4,3))[y<0][x<0]

tests = [[1, 2, 1], [3, 5, 1], [-10, 100, 2], [-1, -9, 3], [19, -56, 4], [1, 1, 1], [-60, -12, 3]]

for x, y, expected in tests:
    print(quadrant(x, y), expected, f"{x = }, {y = }")
