# Aerial Firefighting
# https://www.codewars.com/kata/5d10d53a4b67bb00211ca8af/train/python

# 나의 풀이
def waterbombs(fire, w):
    cnt = 0
    for i in range(w, 0, -1):
        if 'x'*i in fire:
            cnt += fire.count('x'*i)
            fire = fire.replace('x'*i, '')
    return cnt

# 다른 사람의 풀이
from math import ceil
def waterbombs1(fire, w):
  return sum(ceil(len(l)/w) for l in fire.split('Y'))

print(waterbombs("xxxxYxYx", 4), 3)
print(waterbombs("xxYxx", 3), 2)