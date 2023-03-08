# Delta Generators
# https://www.codewars.com/kata/6040b781e50db7000ab35125/train/python

# 나의 풀이 : 못 풀었다
# 이 문제는 next나 pairwise를 사용해야되는 문제이다.
# iter : 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝냅니다.
# next : 반복 가능 객체의 다음 요소 반환
# yeild : 제너레이터 반환
# generator : 여러 개의 데이터를 미리 만들어 놓지 않고 필요할 때마다
# 즉석해서 하나씩 만들어낼 수 있는 객체
def delta(values, n):
    values = iter(values) if n==1 else delta(values, n-1)
    prev = next(values)
    for v in values:
        yield v - prev
        prev = v

from itertools import pairwise
def delta1(values: iter, n: int) -> iter:
    return delta1((b - a for a, b in pairwise(values)), n - 1) if n > 0 else values

first_n = lambda g, n: [next(g) for _ in range(n)]

print(list(delta([1, 2, 3, 4, 5, 6], 1)), [1, 1, 1, 1, 1])
print(list(delta([3, 3, -5, 77], 2)), [-8, 90])
print(list(delta([1.5] * 10, 9)), [0.0])
print(list(delta([1, -1, 1, -1], 3)), [-8])

def ones():
    while True:
        yield 1

print(first_n(delta(ones(), 1), 1000), [0] * 1000)
print(first_n(delta(ones(), 100), 1000), [0] * 1000)

def up():
    a, b = 0, 1
    while True:
        yield a
        a, b = a + b, b + 3

print(first_n(delta(up(), 1), 10), [1, 4, 7, 10, 13, 16, 19, 22, 25, 28])
print(first_n(delta(up(), 2), 10), [3] * 10)

input = [set([6, 2, 'A']), set([2, 'B', 8]), set(['A', 'B'])]
print(list(delta(input, 1)), [{8, 'B'}, {'A'}])
print(list(delta(input, 2)), [{'A'}])
