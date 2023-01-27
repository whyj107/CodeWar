# Let's Play Darts!
# https://www.codewars.com/kata/5870db16056584eab0000006/train/python

# 나의 풀이
# Outside : X
# Bull's eye : 12.70/DB
# Bull : 31.8/SB
# A single number : n
# Triple ring inner : 198/tn
# Triple ring outer : 214
# Double ring inner : 324/dn
# Double ring outer : 340
from math import atan2, pi
def get_score(x, y):
    d = pow(pow(x, 2) + pow(y, 2), 0.5)
    result = ''
    if d <= 12.70/2: return "DB"
    elif d <= 31.8/2: return "SB"
    elif 340/2 < d: return "X"
    elif 198/2 <= d and d <= 214/2: result += 'T'
    elif 324/2 <= d and d <= 340/2: result += 'D'

    angle = atan2(y, x)*180/pi

    if abs(angle) <= 9: result += '6'
    elif abs(angle) <= 27: result += '13' if angle > 0 else '10'
    elif abs(angle) <= 45: result += '4' if angle > 0 else '15'
    elif abs(angle) <= 63: result += '18' if angle > 0 else '2'
    elif abs(angle) <= 81: result += '1' if angle > 0 else '17'
    elif abs(angle) <= 99: result += '20' if angle > 0 else '3'
    elif abs(angle) <= 117: result += '5' if angle > 0 else '19'
    elif abs(angle) <= 135: result += '12' if angle > 0 else '7'
    elif abs(angle) <= 153: result += '9' if angle > 0 else '16'
    elif abs(angle) <= 171: result += '14' if angle > 0 else '8'
    elif abs(angle) <= 189: result += '11'

    return result


from math import atan2, degrees
def get_score1(x, y):
    r, a = (x * x + y * y) ** 0.5, degrees(atan2(y, x)) + 9
    t = str([6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10][int(a + 360 if a < 0 else a) // 18])
    for l, s in [(6.35, 'DB'), (15.9, 'SB'), (99, t), (107, 'T' + t), (162, t), (170, 'D' + t)]:
        if r <= l: return s

    return 'X'

# print(get_score(-133.69, -147.38), "X")
# print(get_score(4.06, 0.71), "DB")
# print(get_score(2.38, -6.06), "SB")
print(get_score(-5.43, 117.95), "20")
print(get_score(-73.905, -95.94), "7")
print(get_score(55.53, -87.95), "T2")
print(get_score(-145.19, 86.53), "D9")
print(get_score(-130, 0), "11")
print(get_score(145.19, 0), "6")
print(get_score(0, 86.53), "20")
print(get_score(0, -86.53), "3")