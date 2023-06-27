# Decimal Time Conversion
# https://www.codewars.com/kata/6397b0d461067e0030d1315e/train/python

# 나의 풀이
# 36 : 0.01
def to_industrial(time):
    if type(time) == int:
        return round(round(time*60/36)*0.01, 2)
    elif type(time) == str:
        t = time.split(':')
        return int(t[0]) + round(round(int(t[1])*60/36)*0.01, 2)


def to_normal(time):
    a = int(time)
    b = round(time%1*100/60*36)
    return f'{a}:{b}' if b >= 10 else f'{a}:0{b}'

# 다른 사람의 풀이
def to_industrial1(time):
    if isinstance(time, str):
        h, m = map(int, time.split(':'))
        time = 60*h + m
    return round(time/60, 2)

def to_normal1(time):
    return f"{int(time)}:{time%1*60:02.0f}"


"""
print(to_industrial(1), 0.02)
print(to_industrial(2), 0.03)
print(to_industrial(3), 0.05)
print(to_industrial(4), 0.07)
print(to_industrial("0:05"), 0.08)
print(to_industrial("0:06"), 0.1)
print(to_industrial("0:07"), 0.12)
print(to_industrial("5:35"), 5.58)
print(to_industrial(135), 2.25)
"""
print(to_normal(1.75), "1:45")
print(to_normal(0.33), "0:20")
print(to_normal(124.60), "124:36")
