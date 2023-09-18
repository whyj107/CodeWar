# Find factors of a number
# https://www.codewars.com/kata/564fa92d1639fbefae00009d/train/python

# 나의 풀이
def factors(x):
    if not isinstance(x, int) or x < 1: return -1
    r = set()
    for i in range(1, int(x**0.5)+1):
        if not x%i:
            r.add(i)
            r.add(x//i)
    r = list(r)
    return sorted(r, reverse=True)

print(factors(-4), -1, "didn't work for -4")
print(factors(0), -1, "didn't work for 0")
print(factors(-12), -1, "didn't work for -12")
print(factors('a'), -1, "didn't work for 'a'")
print(factors(4.5), -1, "didn't work for 4.5")
print(factors('hello world'), -1, "didn't work for 'hello world'")
print(factors(54), [54, 27, 18, 9, 6, 3, 2, 1], "didn't work for 54")
print(factors(49), [49, 7, 1], "didn't work for 49")
print(factors(1), [1], "didn't work for 1")