# Simple Fun #251: Apples Distribution
# https://www.codewars.com/kata/590fca79b5f8a69285000465/train/python

# 문제를 이해하지 못한 문제...

# 풀이
def apples_distribution(apples, capacity, max_left):
    result = 0
    for x in range(1, capacity+1):
        if apples%x <= max_left:
            result += 1
    return result

def apples_distribution1(apples, capacity, max_left):
    return sum(apples % i <= max_left for i in range(1, min(apples, capacity) + 1))

print(apples_distribution(7, 4, 1), 3)
print(apples_distribution(10, 5, 1), 4)