# Find out whether the shape is a cube
# https://www.codewars.com/kata/58d248c7012397a81800005c/train/python

# 나의 풀이
def cube_checker(volume, side):
    if volume <= 0 or side <= 0: return False
    return volume == pow(side, 3)

# 다른 사람의 풀이
def cube_checker1(volume, side):
    return 0 < volume == side**3

print(cube_checker(-12, 2), False)
print(cube_checker(8, 3),  False)
print(cube_checker(8, 2),  True)
print(cube_checker(-8, -2), False, "side or volume < 0 are invalid !")
print(cube_checker(0, 0),  False)
print(cube_checker(27, 3), True)
print(cube_checker(1, 5),  False)
print(cube_checker(125, 5),True)
print(cube_checker(125, -5),False)
print(cube_checker(0, 12), False)
print(cube_checker(12, -1),False)
print(cube_checker(1, 1),  True)