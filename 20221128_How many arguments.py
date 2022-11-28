# How many arguments
# https://www.codewars.com/kata/5c44b0b200ce187106452139/train/python

# 나의 풀이
def args_count(*n, **kwargs):
    print(n, kwargs)
    return len(n) + len(kwargs)

# 다른 사람의 풀이
args_count1=lambda*a,**b:len(a)+len(b)

def args_count1(*args, **kwargs):
    return len([*args, *kwargs])

print(args_count(100), 1)
print(args_count(100, 2, 3), 3)
print(args_count(32, a1=12), 2)
print(args_count(), 0)