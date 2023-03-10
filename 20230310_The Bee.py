# The Bee
# https://www.codewars.com/kata/6408ba54babb196a61d66a65/train/python

# 풀이 : 모르겠따
def the_bee(n):
    m = 2*n-1
    dp = [[0]*m for _ in range(m)]
    for i in range(n):
        dp[i][0] = dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, m):
            if abs(i-j) < n:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
    return dp[m-1][m-1]


print(the_bee(2), 11)
print(the_bee(3), 291)
print(the_bee(5), 259123)
print(the_bee(20), 11419120154603538332020717795)
print(the_bee(33), 706829476133138423874525925298446150375545319299)
print(the_bee(50), 61068096560504518254246449553519425203436341865056944755649047832571626123)