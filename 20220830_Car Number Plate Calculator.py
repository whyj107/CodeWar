# Car Number Plate Calculator
# https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/python

# 풀이
def find_the_number_plate(customer_id):
    q, r = divmod(customer_id, 999)
    q, a = divmod(q, 26)
    c, b = divmod(q, 26)
    return f"{chr(a+97)}{chr(b+97)}{chr(c+97)}{r+1:03d}"

from string import ascii_lowercase
def find_the_number_plate1(n):
    return (
        ascii_lowercase[n // 999 % 26] +
        ascii_lowercase[n // 999 // 26 % 26] +
        ascii_lowercase[n // 999 // 26 // 26 % 26] +
        str(n % 999 + 1).rjust(3, '0'))

CONFIG = [
    (3, 'aaa004'),
    (1487, 'baa489'),
    (40000, 'oba041'),
    (17558423, 'zzz999'),
    (234567, 'aja802'),
    (43056, 'rba100')
]

for inp, exp in CONFIG:
    print(find_the_number_plate(inp), exp)