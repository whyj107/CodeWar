# Summation Triangle
# https://www.codewars.com/kata/6357825a00fba284e0189798/train/python

# 나의 풀이
"""
time over
def get_sum(n):
    result = 0
    for i in range(n+1):
        s = 2*i+i+1
        e = 2*i+n+1
        result += (s+e)*((e-s+1)/2)
    return result

def get_sum(n):
    result = 0
    for i in range(n+1):
        result += sum([2 * j + i + 1 for j in range(i + 1)])
    return result
"""

# 다른 사람의 풀이
def get_sum(n):
    #     a  n += 1 #triangle with size n+1
    #     b = n += 2
    #     c = a * b * (4 * a - 1)
    return (n+1)*(n+2)*(4*n+3)//6

print(get_sum(0), 1)
print(get_sum(1), 7)
print(get_sum(2), 22)
print(get_sum(3), 50)
for i in range(11):
    print(get_sum(i))

print(get_sum(pow(10, 6)))