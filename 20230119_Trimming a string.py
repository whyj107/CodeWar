# Trimming a string
# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python

# 나의 풀이
def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size-3] + '...'


print(trim("Creating kata is fun", 14),"Creating ka...")
print(trim("He", 1),"H...")
print(trim("Hey", 2),"He...")
print(trim("Hey", 3),"Hey")
print(trim("Coding rocks", 12),"Coding rocks")
print(trim("Code Wars is pretty rad", 50), "Code Wars is pretty rad")
print(trim("London is freezing",18),"London is freezing")
