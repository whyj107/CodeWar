# Simple Fun #109:Segment Cover
# https://www.codewars.com/kata/589ac16a0cccbff11d000115/train/python

# 풀이
def segment_cover(A, L):
    n, s = 1, min(A)
    for i in sorted(A):
        if s+L < i:
            s = i
            n += 1
    return n


print(segment_cover([1, 3, 4, 5, 8], 3), 2)
print(segment_cover([-7, -2, 0, -1, -6, 7, 3, 4], 4), 3)
print(segment_cover([1, 5, 2, 4, 3], 1), 3)
print(segment_cover([1, 10, 100, 1000], 1), 4)