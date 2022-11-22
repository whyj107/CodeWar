# Numbers Which Sum of Powers of Its Digits Is The Same Number
# https://www.codewars.com/kata/560a4962c0cc5c2a16000068/train/python

# 나의 풀이
def eq_sum_powdig(hMax, exp):
    result = []
    for i in range(2, hMax+1):
        tmp = sum([int(j)**exp for j in str(i)])
        if i == int(tmp):
            result.append(i)
    return result

# 다른 사람들의 풀이
def eq_sum_powdig1(hMax, exp):
    res = []
    for i in range (2, hMax+1):
        if sum(int(j) ** exp for j in str(i)) == i:
            res.append(i)
    return res

print(eq_sum_powdig(100, 2), [])
print(eq_sum_powdig(1000, 2), [])
print(eq_sum_powdig(200, 3), [153])
print(eq_sum_powdig(370, 3), [153, 370])