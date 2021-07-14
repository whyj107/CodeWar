# HTML dynamic color string generation
# https://www.codewars.com/kata/56f1c6034d0c330e4a001059/train/python

# 처음 보는 유형의 문제라서 풀지 못했다.
# 다른 사람꺼보니까 그냥 랜덤 숫자 쓰는거였잖아
# 퉷.

# 풀이
import random
def generate_color_rgb():
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color_rgb = '#'
    for i in range(0, 6):
        color_rgb += random.choice(num_list)
    return color_rgb

def generate_color_rgb1():
    return f'#{random.randint(0,0xffffff):06x}'

print(generate_color_rgb()[0], '#')
