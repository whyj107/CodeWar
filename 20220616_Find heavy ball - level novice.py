# Find heavy ball - level: novice
# https://www.codewars.com/kata/544047f0cf362503e000036e/train/python

# 나의 풀이
def find_ball(scales):
    for i in range(1, 8, 2):
        l, r = [i-1], [i]
        w = scales.get_weight(l, r)
        if w < 0:
            return l[0]
        elif w > 0:
            return r[0]

# 다른 사람의 풀이
def find_ball1(scales):
    for i in range(0, 8, 2):
        result = scales.get_weight([i], [i + 1])

        if result:
            return i + (result > 0)