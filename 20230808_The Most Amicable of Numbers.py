# The Most Amicable of Numbers
# https://www.codewars.com/kata/56b5ebaa26fd54188b000018/train/python

# 나의 풀이
def amicable_numbers(n1,n2):
    return sum(f(n1))==n2 and sum(f(n2))==n1

def f(n):
    r = [1]
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            r.append(i)
            r.append(n//i)
    return set(r)

# 다른 사람의 풀이
def amicable_numbers1(n1,n2):
    s1 = sum([x for x in range(1, n1) if n1%x==0])
    s2 = sum([x for x in range(1, n2) if n2%x==0])
    return s1 == n2 and s2 == n1

print(amicable_numbers(220, 284), True)
