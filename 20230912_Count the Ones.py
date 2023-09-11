# Count the Ones
# https://www.codewars.com/kata/5519e930cd82ff8a9a000216/train/python

# 나의 풀이
def hamming_weight(x):
    return bin(x).count('1')

# 다른 사람의 풀이
def hamming_weight1(x):
    count = 0
    while x:
        x &= x-1
        count += 1
    return count

print(hamming_weight(10), 2)
print(hamming_weight(21), 3)
