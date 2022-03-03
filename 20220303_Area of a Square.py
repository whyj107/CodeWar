# Area of a Square
# 8kyu
# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python

# 원의 둘레 : ㅣ = 2 * pi * r
# 원의 넓이 : S = pi * r * r
# 부채꼴 호의 길이 : l = 2 * pi * r * 각도 / 360
# 부채꼴의 넓이 : S = pi * r * r * 각도 / 360 = 0.5 * r * l

# 나의 풀이 : 호의 길이로 r을 구한 뒤 r 제곱한 값
from math import pi
def square_area(A):
    return round(pow(A / pi / 0.5, 2), 2)

# 다른 사람의 풀이
def square_area1(A):
    return round((2 * A / pi) ** 2, 2)

print(square_area(2), 1.62)
print(square_area(0), 0)
print(square_area(14.05), 80)
print(square_area(1), 0.41)
print(square_area(100), 4052.85)