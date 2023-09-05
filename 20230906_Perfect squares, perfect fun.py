# Perfect squares, perfect fun
# https://www.codewars.com/kata/5705ca6a41e5be67720012c0/train/python

# 나의 풀이
def square_it(digits):
    t_l = len(str(digits))
    tmp = t_l**.5
    if int(tmp) != tmp:
        return 'Not a perfect square!'
    else:
        return '\n'.join([str(digits)[i:i+int(tmp)]for i in range(0, t_l, int(tmp))])


sample_test_cases = [
    (1, '1'),
    (222, 'Not a perfect square!'),
    (1212, '12\n12'),
    (123123123, '123\n123\n123'),
    (234562342342, 'Not a perfect square!'),
    (88989, 'Not a perfect square!'),
    (112141568, '112\n141\n568'),
]

for n, expected in sample_test_cases:
    print(square_it(n), expected)