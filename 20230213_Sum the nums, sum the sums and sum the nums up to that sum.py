# Sum the nums, sum the sums and sum the nums up to that sum
# https://www.codewars.com/kata/60d2325592157c0019ee78ed/train/python

# 나의 풀이
def sum_of_sums(n):
    t = n*(n+1)*(n+2)//6
    return (t**2+t)//2

# 다른 사람의 풀이
def sum_of_sums1(n):
    S = lambda n: (n*(n+1))//2
    Z = lambda n: (n*(n+1)*(n+2))//6
    return S(Z(n))

print(sum_of_sums(3), 55)
print(sum_of_sums(5), 630)
print(sum_of_sums(100), 14740530850)