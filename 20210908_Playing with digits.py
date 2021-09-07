# Playing with digits
# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

# 나의 풀이
def dig_pow(n, p):
    result = 0
    for idx, i in enumerate(str(n)):
        result += pow(int(i), idx+p)
    return -1 if not result/n == int(result/n) else result//n

print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)