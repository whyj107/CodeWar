# SevenAte9
# https://www.codewars.com/kata/559f44187fa851efad000087/train/python

# 나의 풀이
def seven_ate9(str_):
    result = str_[0]
    for i in range(1, len(str_)-1):
        if str_[i-1] == str_[i+1] == '7' and str_[i]=='9':
            continue
        result += str_[i]
    return result + str_[-1]

# 다른 사람의 풀이
def seven_ate9_1(str_):
    while "797" in str_:
        str_ = str_.replace("797", "77")
    return str_

import re
def seven_ate9_2(str_):
    return re.sub(r'79(?=7)', r'7', str_)