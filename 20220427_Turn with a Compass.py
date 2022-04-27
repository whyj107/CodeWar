# Turn with a Compass
# https://www.codewars.com/kata/61a8c3a9e5a7b9004a48ccc2/train/python

# 나의 풀이
def direction(facing, turn):
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    while turn <= -360: turn += 360
    while turn >= 360: turn -= 360

    tmp = compass.index(facing) + turn//45

    if tmp >= len(compass): tmp -= len(compass)
    return compass[tmp]

# 다른 사람의 풀이
DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
def direction1(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]

print(direction("S", 180),  "N")
print(direction("SE", -45), "E")
print(direction("W", 495),  "NE")