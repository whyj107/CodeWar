# Return the closet number multiple of 10
# https://www.codewars.com/kata/58249d08b81f70a2fc0001a4/train/python

# 나의 풀이
def closest_multiple_10(i):
    return i - i%10 if i%10 < 5 else i + (10 - i%10)

# 다른 사람의 풀이
def closest_multiple_10_1(i):
    return round(i, -1)

print(closest_multiple_10(54), 50)
print(closest_multiple_10(55), 60)