# Find the next perfect square!
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

# 나의 풀이
def find_next_square(sq):
    return (sq**0.5+1)**2 if sq**0.5 == int(sq**0.5) else -1

# 다른 사람의 풀이
import math
def find_next_square1(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1

print(find_next_square(121), 144)
print(find_next_square(625), 676)
print(find_next_square(319225), 320356)
print(find_next_square(15241383936), 15241630849)
print(find_next_square(155), -1)
print(find_next_square(342786627), -1)