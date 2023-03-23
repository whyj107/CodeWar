# Speed Limit
# https://www.codewars.com/kata/635a7827bafe03708e3e1db6/train/python

# 10~19 : 100달러
# 20~29 : 250달러
# 그 이상 : 500달러
# 나의 풀이
def speed_limit(speed, signals):
    penalty = {1:100, 2:250}
    return sum([penalty.get((speed-s)//10, 500) for s in signals if(speed-s)//10>0])

# 다른 사람의 풀이
def fine(speed, limit):
    if speed >= limit + 30:
        return 500
    if speed >= limit + 20:
        return 250
    if speed >= limit + 10:
        return 100
    return 0

def speed_limit1(speed, limits):
    return sum(fine(speed, limit) for limit in limits)

tests = [
    (60, [80, 70, 60], 0),
    (100, [110, 100, 80], 250),
    (130, [140, 130, 100], 500),
    (110, [120, 110, 100], 100),
    (220, [120, 110, 100], 1500),
    (100, [70, 80, 90, 100], 850),
    (0, [15, 25, 35, 46], 0),
    (60, [], 0)
]

for speed, signals, expected in tests:
    print(speed_limit(speed, signals[:]), expected, f"{speed = }, {signals = }")
