# Simple Fun #219: Light Bulbs
# https://www.codewars.com/kata/5901555b63bf404a66000029/train/python

# 나의 풀이
def light_bulbs(lights, n):
    tmp = lights.copy()
    for _ in range(n):
        for i in range(len(lights)):
            if lights[i-1] == 1:
                tmp[i] = 0 if tmp[i] else 1
        lights = tmp.copy()
    return tmp

# 다른 사람의 풀이
def light_bulbs1(lights, n):
    for _ in range(n):
        lights = [lights[i-1] ^ light for i,light in enumerate(lights)]
    return lights

sample_test_cases = [
    ([0, 1, 1, 0, 1, 1], 2, [1, 0, 1, 1, 0, 1]),
    ([0, 0, 1, 1, 1], 5, [1, 1, 1, 0, 1]),
]

for lights, n, expected in sample_test_cases:
    print(light_bulbs(lights, n), expected)