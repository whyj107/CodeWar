# Ball Upwards
# https://www.codewars.com/kata/566be96bb3174e155300001b/train/python

# 나의 풀이
def max_ball(v0):
    # h = v * t - 0.5 * g * t * t
    # h = (v - 0.5 * 9.81 * t) * t
    # 0 = (v - 0.5 * 9.81 * t) * t
    # v = 0.5 * 9.81 * t
    # t = v / (0.5 * 9.81)
    # t = v * 2 / 9.81 - 총 시간
    # t = v / 9.81 - 최고점
    return round(10*v0/9.81/3.6)

print(max_ball(37), 10)
print(max_ball(45), 13)
print(max_ball(99), 28)
print(max_ball(85), 24)