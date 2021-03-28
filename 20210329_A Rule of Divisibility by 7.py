# A Rule of Divisibility by 7
# https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python

# 나의 풀이
def seven(m):
    cnt = 0
    while m > 99:
        m, b = divmod(m, 10)
        m -= 2*b
        cnt += 1
    return (m, cnt)

# 다른 사람의 풀이
def seven1(m, step = 0):
  if m < 100: return (m, step)
  x, y, step = m // 10, m % 10, step + 1
  res = x - 2 * y
  return seven(res, step)

print(seven(1603), (7, 2))
print(seven(371), (35, 1))
print(seven(483), (42, 1))
print(seven(483595), (28, 4))
