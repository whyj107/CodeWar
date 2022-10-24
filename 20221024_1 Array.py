# +1 Array
# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python

# 나의 풀이
def up_array(arr):
    if not arr: return None
    result = []
    plus = 1
    for a in arr[::-1]:
        if a < 0 or a > 9:
            return None
        a += plus
        if a == 10:
            plus = 1
            a = 0
        else:
            plus = 0
        result.append(a)
    if plus: result.append(plus)
    return result[::-1]

# 다른 사람의 풀이
def up_array1(a):
    if not a or any(not 0 <= x < 10 for x in a): return
    for i in range(1, len(a)+1):
        a[-i] = (a[-i] + 1) % 10
        if a[-i]: break
    else: a[:0] = [1]
    return a

print(up_array([2, 3, 9]), [2, 4, 0])
print(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
print(up_array([1, -9]), None)
print(up_array([9, 9]), [1, 0, 0])
print(up_array([0, 4, 2]), [0, 4, 3])