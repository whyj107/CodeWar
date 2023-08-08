# The mean of two means
# https://www.codewars.com/kata/583df40bf30065fa9900010c/train/python

# 나의 풀이
def get_mean(arr,x,y):
    if x < 2 or y > len(arr) or y < 2: return -1
    return (sum(arr[:x])/x + sum(arr[-y:])/y)/2

# 다른 사람의 풀이
def get_mean1(arr,x,y):
    if 1 < x <= len(arr) and 1 < y <= len(arr):
       return (sum(arr[:x])/x+sum(arr[-y:])/y)/2
    return -1

print(get_mean([1, 3, 2, 4], 2, 3), 2.5)
print(get_mean([1, 3, 2], 2, 2), 2.25)
print(get_mean([1, 3, 2, 4], 1, 2), -1)
print(get_mean([1, 3, 2, 4], 2, 8), -1)
print(get_mean([1, -1, 2, -1], 2, 3), 0)