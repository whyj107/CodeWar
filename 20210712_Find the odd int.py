# Find the odd int
# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

# 나의 풀이
from collections import Counter
def find_it(seq):
    return sum([i for i in Counter(seq) if Counter(seq)[i] % 2 != 0])

# 다른 사람의 풀이
def find_it1(seq):
    return [x for x in seq if seq.count(x) % 2][0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
print(find_it([10]), 10);
print(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
print(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);