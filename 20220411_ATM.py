# ATM
# https://www.codewars.com/kata/5635e7cb49adc7b54500001c/train/python

# 나의 풀이
# 10, 20, 50, 100, 200, 500
def solve(n):
    cnt = 0
    for c in [500, 200, 100, 50, 20, 10]:
        if n >= c:
            cnt += (n//c)
            n -= (n//c*c)
    return -1 if n != 0 else cnt

# 다른 사람의 풀이
def solve1(n):
    if n%10: return -1
    c, billet = 0, iter((500,200,100,50,20,10))
    while n:
        x, r = divmod(n, next(billet))
        c, n = c+x, r
    return c



print(solve(770), 4)
print(solve(550), 2)
print(solve(10), 1)
print(solve(1250), 4)
print(solve(1500), 3)

print(solve(125), -1)
print(solve(666), -1)
print(solve(42), -1)