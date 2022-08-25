# The maximum sum value of ranges - Challenge version
# https://www.codewars.com/kata/583d171f28a0c04b7c00009c/train/python

# 나의 풀이
# 시간 초과 발생
def max_sum0(a, ranges):
    return max(sum(a[i:j+1]) for i, j in ranges)

# 다른 사람의 풀이
# accumulate : 누적 결과를 반환하는 이터레이터를 만든다.
# itertools.accumulate(iterable[, func])

from itertools import accumulate
def max_sum1(a, ranges):
    prefix = list(accumulate(a, initial=0))
    return max(prefix[j+1] - prefix[i] for i,j in ranges)

def max_sum(a, r):
    check = list(accumulate(a))+[0]
    return max(check[j]-check[i-1] for i, j in r)

print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1],
              [(1, 3), (0, 4), (6, 8)]), 6)
print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1],
              [(1, 3)]), 5)
print(max_sum([1, -2, 3, 4, -5, -4, 3, 2, 1],
              [(1, 4), (2, 5)]), 0)