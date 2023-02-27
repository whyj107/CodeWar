# Simple Fun #34: Numbers Grouping
# https://www.codewars.com/kata/588711735ea0b4649e000001/train/python

# 나의 풀이
# 1 ~ 10000
# 10^4+1 ~ 2x10^4
# ...
def numbers_grouping(a):
    dic = {}
    for _ in a:
        dic.setdefault(_//10001, 0)
        dic[_//10001] += 1
    return len(dic.keys()) + sum(dic.values())

# 다른 사람의 풀이
def numbers_grouping1(a):
    return len(set((n-1)//10000 for n in a))+len(a)

print(numbers_grouping([20000, 239, 10001, 999999, 10000, 20566, 29999]), 11)
print(numbers_grouping([10000, 20000, 30000, 40000, 50000, 60000, 10000, 120000, 150000, 200000, 300000, 1000000]), 23)
print(numbers_grouping([10000]), 2)
print(numbers_grouping([10000, 1]), 3)