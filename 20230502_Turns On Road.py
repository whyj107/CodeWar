# Simple Fun #288: Turns On Road
# https://www.codewars.com/kata/591c075a94414c1617000063/train/python

# 풀이 : 내가 못 풀었음
def turns_on_road(x, y):
    if [x, y] == [0, 0]: return 0
    if x > 0 and -x + 1 < y <= x: return 4 * x - 3
    if x < 0 and x <= y < -x: return 4 * (-x) - 1
    if y > 0 and -y <= x < y: return 4 * y - 2
    if y < 0 and y < x <= -y + 1: return 4 * (-y)

print(turns_on_road(1,1),1)
print(turns_on_road(1,-1),4)
print(turns_on_road(0,1),2)
print(turns_on_road(-1,-1),3)
print(turns_on_road(10,10),37)
print(turns_on_road(0,0),0)
print(turns_on_road(2,-1),4)
print(turns_on_road(2,2),5)
print(turns_on_road(3,5),18)
print(turns_on_road(694481,703630),2814518)
print(turns_on_road(875286,925200),3700798)
print(turns_on_road(1000000,1000000),3999997)