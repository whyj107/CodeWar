# Asperand pixel counting
# https://www.codewars.com/kata/63d54b5d05992e0046752389/train/python

# 나의 풀이
def count_pixels(k):
    return max(11, 8*k+2)

# 다른 사람의 풀이
count_pixels1=lambda k:8*k+2+(k<2)

print(count_pixels(1), 11)
print(count_pixels(2), 18)
print(count_pixels(3), 26)
print(count_pixels(4), 34)