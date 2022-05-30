# Tank Truck
# https://www.codewars.com/kata/55f3da49e83ca1ddae0000ad/train/python

# 수학 문제
# 친절한 설명
import math
def tankvol(h, d, vt):
    r = d/2.0
    if h == r: return vt/2     # h가 r과 같은 값일 경우
    half = h>r                 # h가 r보다 클 경우 half는 true
    h = d-h if half else h     # half를 토대로 h 값 재 설정
    a = r-h                    # 삼각형 직선 길이 구하기
    b = math.sqrt(r**2-a**2)   # 다른 삼각형 변 길이 구하기
    t = 2*math.asin(b/r)       # 각도 구하기
    A = r**2*t/2 - b*a         # 넓이 구하기
    v = vt*A/(math.pi*r**2)    # 부피 구하기
    return int(vt-v) if half else int(v)

# 각도 구하여 계산
def tankvol1(h, d, vt):
    r = d/2
    theta = math.acos((r-h)/r)
    return int(vt*(theta-math.sin(theta)*(r-h)/r)/math.pi)

print(tankvol(5, 7, 3848), 2940)
print(tankvol(2, 7, 3848), 907)
print(tankvol(40, 120, 3500), 1021)
print(tankvol(60, 120, 3500), 1750)
print(tankvol(80, 120, 3500), 2478)