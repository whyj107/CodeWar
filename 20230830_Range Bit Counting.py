# Range Bit Counting
# https://www.codewars.com/kata/58845748bd5733f1b300001f/train/python

# 나의 풀이
def range_bit_count(a, b):
    return sum([bin(i).count('1') for i in range(a, b+1)])

# 다른 사람의 풀이
def range_bit_count1(a,b):
    return sum(x.bit_count() for x in range(a,b+1))

print(range_bit_count(2, 7), 11)
print(range_bit_count(0, 1), 1)
print(range_bit_count(4, 4), 1)