# Length and two values
# https://www.codewars.com/kata/62a611067274990047f431a8/train/python

# 나의 풀이
def alternate(n, first_value, second_value):
    return [first_value if i%2==0 else second_value for i in range(n)]

# 다른 사람의 풀이
def alternate1(n, first_value, second_value):
    return [[first_value, second_value][i % 2] for i in range(n)]

print(alternate(5, True, False), [True, False, True, False, True])
print(alternate(20, "blue", "red"), ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red'])
print(alternate(0, "lemons", "apples"), [])
