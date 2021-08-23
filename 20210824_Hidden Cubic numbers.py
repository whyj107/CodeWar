# Hidden "Cubic" numbers
# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python

# 나의 풀이
def is_sum_of_cubes(s):
    n = ''
    result = []
    for i in s+'.':
        if i.isnumeric():
            n += i
        if len(n) == 3 or (not i.isnumeric() and len(n) != 0):
            if iscubeNum(n):
                result.append(n)
            n = ''
    return "Unlucky" if len(result) == 0 else f"{' '.join(result)} {sum(map(int, result))} Lucky"

def iscubeNum(n):
    return sum([int(i)**3 for i in n]) == int(n)

# 다른 사람의 풀이
import re
PATTERN = re.compile(r'(\d{1,3})')
def is_sum_of_cubes1(s):
    found = list(filter(lambda nStr: int(nStr) == sum(int(d)**3 for d in nStr), PATTERN.findall(s)))
    return "Unlucky" if not found else "{} {} {}".format(' '.join(found), sum(map(int, found)), 'Lucky')

# -----------------------------------------------------------------------------------------
def go_test(test_val, expected_val):
    print(is_sum_of_cubes(test_val), expected_val)

go_test("&z _upon 407298a --- ???ry, ww/100 I thought, 631str*ng and w===y -721&()", "407 407 Lucky")
go_test("No numbers!", "Unlucky")
go_test("0 9026315 -827&()", "0 0 Lucky")
