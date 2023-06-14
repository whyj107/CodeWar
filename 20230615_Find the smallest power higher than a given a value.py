# Find the smallest power higher than a given a value
# https://www.codewars.com/kata/56ba65c6a15703ac7e002075/train/python

# 나의 풀이
def find_next_power(val, pow_):
    result = 0
    idx = 1
    while result < val:
        result = pow(idx, pow_)
        idx += 1
    return result

# 다른 사람의 풀이
def find_next_power1(val, pow_):
    return int(val ** (1.0 / pow_) + 1) ** pow_

print(find_next_power(12385, 3), 13824)
print(find_next_power(1245678, 5), 1419857)
print(find_next_power(1245678, 6), 1771561)