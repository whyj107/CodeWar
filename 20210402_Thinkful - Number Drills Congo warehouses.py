# Thinkful - Number Drills: Congo warehouses
# https://www.codewars.com/kata/5862e7c63f8628a126000e18/train/python

# 나의 풀이
def box_capacity(length, width, height):
    length = (length * 12)//16
    width = (width * 12)//16
    height = (height*12)//16
    return length * width * height

# 다른 사람의 풀이
def box_capacity1(l, w, h):
    return ((l * 3) // 4) * ((w * 3) // 4) * ((h * 3) // 4)

print(box_capacity(70, 60, 15), 25740)
# print(box_capacity(32, 64, 16), 13824)
# print(box_capacity(20, 20, 20), 3375)
# print(box_capacity(80, 40, 20), 27000)