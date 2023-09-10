# Hold Your Breath!
# https://www.codewars.com/kata/64fbfa3518692c2ed0ebbaa2/train/python

# 나의 풀이
def diving_minigame(lst):
    s = 10
    for l in lst:
        s += (-2) if l<0 else 4
        s = 10 if s>10 else s
        if s == 0: return False
    return s > 0

print(diving_minigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), True)
print(diving_minigame([-5, -15, -4, 0, 5]), True)
print(diving_minigame([0, -4, 0, -4, -5, -2]), True)
print(diving_minigame([-4, -3, -4, -3, 5, 2, -5, -20, -42, -4, 5, 3, 5]), True)
print(diving_minigame([-3, -6, -2, -6, -2]), False)
print(diving_minigame([1, 2, 1, 2, 1, 2, 1, 2, 1, -3, -4, -5, -3, -4]), False)
print(diving_minigame([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2]), False)
print(diving_minigame([20, 3, 4, -20, 14, 3, 8, -18, -20, -13, 13, -14, -12, -1, 20, -6, -20, -2]), False)