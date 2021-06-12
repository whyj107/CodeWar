# Find the Squares
# https://www.codewars.com/kata/60908bc1d5811f0025474291/train/python

# 나의 풀이
# a**2 = c**2 - b**2
# a**2 = (n+1)**2 - n**2
# a**2-1 = 2n
# n = (a**2-1)//2
def find_squares(num):
    return f'{((num-1)//2+1)**2}-{((num-1)//2)**2}'

# 다른 사람의 풀이
def find_squares1(num):
    for i in range(0,1000000):
        if (i+1)*(i+1)-i*i == num:
            return f"{(i+1)*(i+1)}-{i*i}"

print(find_squares(9), '25-16')
print(find_squares(5), '9-4')
print(find_squares(7), '16-9')
