# Validate Credit Card Number
# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/train/python

# 나의 풀이
def validate(n):
    l = list(map(int, str(n)))
    start = 0 if len(l)%2 == 0 else 1

    for i in range(start, len(l), 2):
        l[i] *= 2
        if l[i] > 9: l[i] -= 9

    return sum(l)%10 == 0

print(validate(1714), False)
print(validate(12345), False)
print(validate(891), False)
print(validate(123), False)
print(validate(1), False)
print(validate(2121), True)
print(validate(1230), True)