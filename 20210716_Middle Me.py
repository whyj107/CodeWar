# Middle Me
# https://www.codewars.com/kata/59cd155d1a68b70f8e000117/train/python

# 나의 풀이
def middle_me(N, X, Y):
    return Y*(N//2) + X + Y*(N//2) if N%2 == 0 else X

# 다른 사람의 풀이 : 람다
middle_me1=lambda N,X,Y:(X.center(N+1,Y),X)[N%2]

print(middle_me(18, 'z', '#'), '#########z#########')
print(middle_me(19, 'z', '#'), 'z')