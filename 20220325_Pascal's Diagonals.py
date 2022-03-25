# Pascal's Diagonals
# https://www.codewars.com/kata/576b072359b1161a7b000a17/train/python

# 나의 풀이
def generate_diagonal(n, l):
    pascal = pascals_triangle(n, l + n)
    return [p[idx] for idx, p in enumerate(pascal)]

def pascals_triangle(n, l):
    triangle = [[1]]
    for _ in range(l - 1):
        to_sum = zip([0] + triangle[-1], triangle[-1] + [0])
        triangle.append(list(map(sum, to_sum)))
    return triangle[n:]

# 다른 사람의 풀이
def generate_diagonal1(d, l):
    result = [1] if l else []
    for k in range(1, l):
        result.append(result[-1] * (d+k) // k)
    return result

print(generate_diagonal(2, 5), [1, 3, 6, 10, 15])
print(generate_diagonal(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(generate_diagonal(3, 7), [1, 4, 10, 20, 35, 56, 84])