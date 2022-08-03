# Count the divisible numbers
# https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python

# 나의 풀이
def divisible_count(x, y, k):
    return y//k - x//k + (1 if x/k==x//k else 0)

# 다른 사람의 풀이
def divisible_count1(x,y,k):
    return y//k - (x-1)//k

print(divisible_count(6, 11, 2),3)