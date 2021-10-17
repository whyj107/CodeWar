# Keypad horror
# https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python

# 나의 풀이
def computer_to_phone(numbers):
    n = {'1': '7', '2': '8', '3': '9', '7': '1', '8': '2', '9': '3'}
    return ''.join([n.get(i, i) for i in numbers])

# 다른 사람의 풀이
from string import maketrans

def computer_to_phone(numbers):
    return numbers.translate(maketrans("123789", "789123"))

print(computer_to_phone("0789456123"), "0123456789")
print(computer_to_phone("000"), "000")
print(computer_to_phone("94561"), "34567")