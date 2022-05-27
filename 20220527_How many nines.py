# How many nines?
# https://www.codewars.com/kata/5e18743cd3346f003228b604/train/python

# 다른 사람의 풀이
def nines(n):
    s, l = str(n), len(str(n))
    result = 0
    for i in range(l):
        j = l - i - 1
        result += int(s[i]) * (10**j - 9**j)
        if s[i] == '9':
            result += 1
            if i < l-1:
                result += int(s[i+1:])
            break
    return result

from re import sub
def nines1(n):
    return n - int(sub(r'9.*$', lambda m: '8'*len(m[0]), str(n)), 9)

print(nines(1), 0)
print(nines(10), 1)
print(nines(100), 19)
print(nines(1000), 271)
print(nines(3950), 1035)

result = [1 for i in range(1000, 2000) if '9' in str(i)]
print(sum(result))