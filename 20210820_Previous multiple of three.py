# Previous multiple of three
# https://www.codewars.com/kata/61123a6f2446320021db987d/train/python

# 나의 풀이
def prev_mult_of_three(n):
    while n > 2:
        if n%3 == 0 :
            return n
        n //= 10

# 다른 사람의 풀이
def prev_mult_of_three1(n):
    while n % 3:
        n //= 10
    return n or None

print(prev_mult_of_three(1), None)
print(prev_mult_of_three(25), None)
print(prev_mult_of_three(36), 36)
print(prev_mult_of_three(1244), 12)
print(prev_mult_of_three(952406), 9)