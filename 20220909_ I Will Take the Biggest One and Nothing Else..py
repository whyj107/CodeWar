# I Will Take the Biggest One and Nothing Else.
# https://www.codewars.com/kata/631082840289bf000e95a334/train/python

# 나의 풀이
def max_int_chain(n):
    if n < 5:
        return -1
    elif n % 2 == 0:
        return (n//2-1)*(n//2+1)
    else:
        return (n//2) *(n//2+1)

# 다른 사람의 풀이
def max_int_chain1(n):
    x = n-1>>1
    return -1 if n<5 else x * (n-x)

print(max_int_chain(6), 8)
print(max_int_chain(10), 24)
print(max_int_chain(26), 168)
print(max_int_chain(32), 255)
print(max_int_chain(36), 323)
print(max_int_chain(39), 380)

print(max_int_chain(5), 6)
print(max_int_chain(7), 12)
print(max_int_chain(11), 30)
print(max_int_chain(13), 42)
print(max_int_chain(17), 72)

print(max_int_chain(1), -1)
print(max_int_chain(2), -1)
print(max_int_chain(3), -1)
print(max_int_chain(4), -1)
