# Mysterious Singularity Numbers
# https://www.codewars.com/kata/6409aa6df4a0b773ce29cc3d/train/python

# 나의 풀이
def real_numbers(n):
    return n - (n//2 + n//3 + n//5) + (n//6 + n//10 + n//15) - n//30

print(real_numbers(5), 1)
print(real_numbers(10), 2)
print(real_numbers(20), 6)
print(real_numbers(30), 8)
print(real_numbers(40), 10)
print(real_numbers(55), 15)
print(real_numbers(66), 17)
print(real_numbers(75), 20)
print(real_numbers(100), 26)