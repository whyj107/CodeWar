# Happy Birthday
# https://www.codewars.com/kata/5d65fbdfb96e1800282b5ee0/train/python

# 나의 풀이
def wrap(height, width, length):
    return (sum([height, width, length])+min(height, width, length))*2+20

# 다른 사람의 풀이
def wrap1(*dims):
    return sum(dims, min(dims))*2 + 20

print(wrap(17, 32, 11), 162)
print(wrap(13, 13, 13), 124)
print(wrap(1, 3, 1), 32)