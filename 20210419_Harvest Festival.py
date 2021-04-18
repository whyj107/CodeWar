# Harvest Festival
# https://www.codewars.com/kata/606efc6a9409580033837dfb/train/python

# 나의 풀이
def plant(seed, water, fert, temp):
    result = ''
    if 20 <= temp <= 30:
        for i in range(water):
            result += '-' * water + seed * fert
    else:
        result = '-'*water*water + seed
    return result

# 다른 사람의 풀이
def plant1(seed, water, fert, temp):
    return ('-' * water + seed * fert) * water if temp >= 20 and temp <= 30 else ('-' * water) * water + seed

print(plant(",", 3, 7, 25) == "---,,,,,,,---,,,,,,,---,,,,,,,")
print(plant("+", 1, 3, 15) == "-+")
print(plant(";", 9, 10, 30) == "---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;---------;;;;;;;;;;")