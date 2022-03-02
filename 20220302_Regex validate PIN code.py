# Regex validate PIN code
# 7kyu
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

# 나의 풀이
def validate_pin(pin):
    return True if pin.isnumeric() and len(pin) in [4, 6] else False

# 다른 사람의 풀이
def validate_pin1(pin):
    return len(pin) in (4, 6) and pin.isdigit()

import re
def validate_pin2(pin):
    return bool(re.fullmatch("\d{4}|\d{6}", pin))

print(validate_pin("1"), False)
print(validate_pin("12"), False)
print(validate_pin("123"), False)
print(validate_pin("12345"), False)
print(validate_pin("1234567"), False)
print(validate_pin("-1234"), False)
print(validate_pin("-12345"), False)
print(validate_pin("1.234"), False)
print(validate_pin("00000000"), False)

print(validate_pin("a234"), False)
print(validate_pin(".234"), False)

print(validate_pin("1234"), True)
print(validate_pin("0000"), True)
print(validate_pin("1111"), True)
print(validate_pin("123456"), True)
print(validate_pin("098765"), True)
print(validate_pin("000000"), True)
print(validate_pin("123456"), True)
print(validate_pin("090909"), True)