# Square Every Digit
# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

# 나의 풀이
def square_digits(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))

print(square_digits(9119), 811181)
print(square_digits(0), 0)