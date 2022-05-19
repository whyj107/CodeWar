# Incrementer
# https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python

# 나의 풀이
def incrementer(nums):
    return [(n + idx + 1) % 10 for idx, n in enumerate(nums)]

# 다른 사람의 풀이
incrementer1=lambda _:[int(str(i+j)[-1]) for j,i in enumerate(_,1)]

print(incrementer([]), [])
print(incrementer([1, 2, 3]), [2, 4, 6])
print(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])
print(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]), [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])