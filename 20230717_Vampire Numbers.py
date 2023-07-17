# Vampire Numbers
# https://www.codewars.com/kata/54d418bd099d650fa000032d/train/python

# 나의 풀이
from collections import Counter
def vampire_test(x, y):
    if x < 0 and y < 0: return False
    return Counter(str(x*y)) == Counter(str(x)+str(y))

# 다른 사람의 풀이
def vampire_test1(x, y):
    return sorted(str(x * y)) == sorted(str(x) + str(y))

print(vampire_test(21, 6) == True, "Basic: 21 * 6 = 126 should return True")
print(vampire_test(204, 615) == True, "Basic: 204 * 615 = 125460 should return True")
print(vampire_test(30, -51) == True, "One Negative: 30 * -51 = -1530 should return True")
print(vampire_test(-246, -510) == False,
            "Double Negatives: -246 * -510 = 125460 should return False (The negative signs aren't present on the product)")
print(vampire_test(210, 600) == True, "Trailing Zeroes: 210 * 600 = 126000 should return True")