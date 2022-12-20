# Survive the attack
# https://www.codewars.com/kata/634d0f7c562caa0016debac5/train/python

# 나의 풀이
def is_defended(attackers, defenders):
    pre_a, cnt_a = sum(attackers), len(attackers)
    pre_d, cnt_d = sum(defenders), len(defenders)
    for a, d in zip(attackers, defenders):
        if a == d:
            cnt_a -= 1
            cnt_d -= 1
        elif a > d:
            cnt_d -= 1
        elif a < d:
            cnt_a -= 1
    return pre_a <= pre_d if cnt_a == cnt_d else cnt_a < cnt_d


print(is_defended([2, 9, 9, 7], [ 1, 1, 3, 8]), False)
print(is_defended([1, 3, 5, 7], [2, 4, 6, 8]), True)
print(is_defended([10, 10, 1, 1], [4, 4, 7, 7]), True)
print(is_defended([], [1, 2, 3]), True)
print(is_defended([1, 2, 3], []), False)
print(is_defended([6, 1, 28, 28], [39, 7]), False)
print(is_defended([3, 17], [18]), False)
print(is_defended([4, 9, 18, 6, 45, 39, 6, 26, 19], [5, 15, 7, 28, 50, 7, 34]), True)
