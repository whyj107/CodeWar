# Simple Fun #112: Array Erasing
# https://www.codewars.com/kata/589d1c08cc2e997caf0000e5/train/python

# 나의 풀이
def array_erasing(lst):
    result = 0
    while len(lst) > 0:
        if len(set(lst)) == 1:
            result += 1
            break
        pre = -1
        conti = False
        tmp = []
        for i in lst:
            if pre != i:
                if not conti:
                    tmp.append(i)
                conti = False
            else:
                conti = True
            pre = i

        if lst == tmp:
            del tmp[len(tmp)//2]
        lst = tmp
        result += 1
    return result

for input, expected in [
    # ([0, 1, 1, 1, 0],                               2),
    # ([0, 1],                                        2),
    ([1, 0, 1, 0],                                  3),
    ([1, 1, 0, 0, 1, 1, 0],                         3),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0],                   3),
    ([1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1], 3),
    ([0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],          3),
    ([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],    3),
    ([1, 0, 1, 0, 1, 0, 0, 1],                      5),
    ([0, 0, 0, 1, 0, 0],                            3),
    ([1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],    6),]:
    print(array_erasing(input), expected)