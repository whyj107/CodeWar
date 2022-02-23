# What century is it?
# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

# 나의 풀이
def what_century(year):
    century = int(year)//100 + (0 if year.endswith('00') else 1)
    return f'{ century }{ {1: "st", 2: "nd", 3: "rd"}.get(century%10, "th") if not century in [11, 12, 13] else "th" }'

# 다른 사람의 풀이
def what_century1(year):
    n = (int(year) - 1) // 100 + 1
    return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))

print(what_century("2011"), "21st")
print(what_century("2154"), "22nd")
print(what_century("2259"), "23rd")
print(what_century("1234"), "13th")
print(what_century("1023"), "11th")
print(what_century("6700"), "67th")