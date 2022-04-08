# nth Floyd line
# https://www.codewars.com/kata/5b096efeaf15bef812000010/train/python

# 나의 풀이
def nth_floyd(n):
    tmp, cnt = 1, 1
    while n > tmp:
        cnt += 1
        tmp += cnt
    return cnt

# 다른 사람의 풀이
def nth_floyd1(n):
  return ((1+8*(n-1))**0.5+1)//2

testc = [
  [15, 5],
  [26, 7],
  [17, 6],
  [24, 7],
  [19, 6],
  [5, 3],
  [212, 21]
]

for n, s in testc:
    soln = s
    print(nth_floyd(n), soln)
