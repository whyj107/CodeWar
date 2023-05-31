# Product of Largest Pair
# https://www.codewars.com/kata/5784c89be5553370e000061b/train/python

# 나의 풀이
def max_product(a):
    n1 = a.pop(a.index(max(a)))
    n2 = a.pop(a.index(max(a)))
    return n1*n2

# 다른 사람의 풀이
import heapq
def max_product1(a):
    x = heapq.nlargest(2,a)
    return x[0]*x[1]

print(max_product([2, 1, 5, 0, 4, 3]) )
"""
print(max_product([56, 335, 195, 443, 6, 494, 252]), 218842)
print(max_product([154, 428, 455, 346]), 194740)
print(max_product([39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411]), 187827)
print(max_product([136, 376, 10, 146, 105, 63, 234]), 87984)
print(max_product([354, 463, 165, 62, 472, 53, 347, 293, 252, 378, 420, 398, 255, 89]), 218536)
print(max_product([346, 446, 26, 425, 432, 349, 123, 269, 285, 93, 75, 14]), 192672)
print(max_product([134, 320, 266, 299]), 95680)
print(max_product([114, 424, 53, 272, 128, 215, 25, 329, 272, 313, 100, 24, 252]), 139496)
print(max_product([375, 56, 337, 466, 203]), 174750)
"""