# Two Sets of Equal Sum
# https://www.codewars.com/kata/647518391e258e80eedf6e06/train/python

# 나의 풀이 : 시간 초과 발생
def create_two_sets_of_equal_sum(n):
    tmp = n*(n+1)/4
    if int(tmp) != tmp: return []
    nums1 = list(range(1, n+1))
    nums2 = []
    while sum(nums1) != sum(nums2):
        num = sum(nums1)-int(tmp)
        if num not in nums1:
            nums2.append(nums1.pop())
        else:
            nums1.remove(num)
            nums2.append(num)
    return [nums1, nums2]

# 다른 사람의 풀이 : 이런 간단한 방법이 있었다니...
def create_two_sets_of_equal_sum1(n):
    r = [*range(1, n + 1)]
    a = r[0::4] + r[1+2*(n%2==0)::4]
    b = r[2::4] + r[1+2*(n%2!=0)::4]
    return [a, b] if sum(a) == sum(b) else []

import random
for i in range(1, 11):
    print(i, create_two_sets_of_equal_sum(i))

for i in range(5):
    n = random.randint(10, 1000)
    print(n, create_two_sets_of_equal_sum(n))

print(create_two_sets_of_equal_sum(1000000))