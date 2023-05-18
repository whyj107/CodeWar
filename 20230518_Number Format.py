# Number Format
# https://www.codewars.com/kata/565c4e1303a0a006d7000127/train/python

# 나의 풀이
def number_format(n):
    return f'{n:,}'

# 다른 사람의 풀이
def number_format1(n):
    return format(n, ',')

print(number_format(100000), "100,000")
print(number_format(5678545), "5,678,545")
print(number_format(-420902), "-420,902")
print(number_format(-3), "-3")
print(number_format(-1003), "-1,003")