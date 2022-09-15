# Complete The Pattern
# https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/python

# 나의 풀이
def pattern0(n):
    result = []
    for i in range(1, n+1):
        result.append(f'{str(i)*i}')
    return '\n'.join(result)

def pattern(n):
    return '\n'.join([f'{str(i)*i}' for i in range(1, n+1)])

# 다른 사람의 풀이
def pattern1(n):
    return '\n'.join(str(i) * i for i in xrange(1, n + 1))

print(pattern(1), "1")
print(pattern(2), "1\n22")
print(pattern(5), "1\n22\n333\n4444\n55555")
print(pattern(0), "")
print(pattern(-25), "")