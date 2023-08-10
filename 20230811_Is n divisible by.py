# Is n divisible by (...)?
# https://www.codewars.com/kata/558ee8415872565824000007/train/python

# 나의 풀이
def is_divisible(*arg):
    return all([arg[0]%i==0 for i in arg])

# 다른 사람의 풀이
def is_divisible1(n, *args):
    return all(not n % i for i in args)

print(is_divisible(3,3,4),False)
print(is_divisible(12,3,4),True)
print(is_divisible(8,3,4,2,5),False)