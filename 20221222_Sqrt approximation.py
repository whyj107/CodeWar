# Sqrt approximation
# https://www.codewars.com/kata/52ecde1244751a799b00018a/train/python

# 나의 풀이
def sqrt_approximation(number):
    s = pow(number, 0.5)
    return int(s) if s == int(s) else [int(s), int(s)+1]

# 다른 사람의 풀이
def sqrt_approximation1(number):
    q, r = divmod(.5.__rpow__(number), 1)
    return [q, q+1] if r else q

print(sqrt_approximation(4), 2)
print(sqrt_approximation(9), 3)
print(sqrt_approximation(16), 4)
print(sqrt_approximation(49), 7)
print(sqrt_approximation(5), [2, 3])
print(sqrt_approximation(85), [9, 10])
print(sqrt_approximation(105), [10, 11])
print(sqrt_approximation(10023), [100, 101])
