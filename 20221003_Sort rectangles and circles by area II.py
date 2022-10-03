# Sort rectangles and circles by area II
# https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/train/python

# 나의 풀이
def sort_by_area(seq):
    result = []
    for s in seq:
        if type(s) == tuple:
            result.append((s[0]*s[1], s))
        else:
            result.append((s*s*3.14, s))
    return [j for i, j in sorted(result)]


# 다른 사람의 풀이
def sort_by_area1(seq):
    def func(x):
        if isinstance(x, tuple):
            return x[0] * x[1]
        else:
            return 3.14 * x * x
    return sorted(seq, key=func)

print(sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ]),
      [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ] )
print(sort_by_area([ (2, 5), 6 ]), [
    (2, 5), 6 ])
print(sort_by_area([]), [] )