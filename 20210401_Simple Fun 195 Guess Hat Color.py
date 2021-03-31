# Simple Fun #195: Guess Hat Color
# https://www.codewars.com/kata/58c21c4ff130b7cab400009e/train/python

# 나의 풀이
def guess_hat_color(a, b, c, d):
    return 2 if b!=c else 1

print(guess_hat_color("white", "black", "white", "black"),2)
print(guess_hat_color("white", "black", "black", "white"),1)