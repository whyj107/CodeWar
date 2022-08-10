# The Supermarket Queue
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

# 나의 풀이
def queue_time(customers, n):
    result = [0]*n
    for c in customers:
        tmp = result.index(min(result))
        result[tmp] += c
    return max(result)

# 다른 사람의 풀이
import heapq
def queue_time1(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)

print(queue_time([], 1), 0)
print(queue_time([5], 1), 5)
print(queue_time([2], 5), 2)
print(queue_time([1, 2, 3, 4, 5], 1), 15)
print(queue_time([1, 2, 3, 4, 5], 100), 5)
print(queue_time([2, 2, 3, 3, 4, 4], 2), 9)