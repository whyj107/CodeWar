# Robot on a Table
# https://www.codewars.com/kata/61aa487e73debe0008181c46/train/python

#  풀이
def robot(n, m, s):
    x, y, xmin, ymin, xmax, ymax = 0, 0, 0, 0, 0, 0
    for i in s:
        # 현재 x, y 좌표
        y += (i=='D') - (i=='U')
        x += (i=='R') - (i=='L')
        # x, y 범위를 위한 min, max 값 설정
        xmin = min(xmin, x)
        ymin = min(ymin, y)
        xmax = max(xmax, x)
        ymax = max(ymax, y)
        # x와 y의 범위에서 현재 x, y가 넘어갈 경우 멈춤
        # x와 y에서 - 값을 했을 경우 더해줌 ('L', 'U')
        if xmax - xmin + 1 > m or ymax - ymin + 1 > n:
            xmin += i=='L'
            ymin += i=='U'
            break
    return 1 - ymin, 1 - xmin

print(robot(3, 3, "RRDLUU"), (2, 1))
print(robot(1, 1, "L"), (1, 1))
print(robot(1, 2, "L"), (1, 2))
# print(robot(4, 3, "LUURRDDLLLUU"), (3, 2))
# print(robot(5, 3, "URDL"), (2, 1))
# print(robot(3, 3, "LURDRDLU"), (2, 2))