# Parabolic Arc Length
# https://www.codewars.com/kata/562e274ceca15ca6e70000d3/train/python

# 풀이
from math import sqrt
def len_curve(n):
    return round(sum(sqrt((2*k+1)**2/n/n + 1) for k in range(n))/n, 9)

print(len_curve(1), 1.414213562)
print(len_curve(10), 1.478197397)