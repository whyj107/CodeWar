# 문제
# The purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expresion with a single, one character variable, and expands it.
# The expresion is in the form (ax+b)^n where a and b are integers
# which may be positive or negative, x is any one character long variable, and n is a natural number.
# If a = 1, no coeficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f...
# where a, c, and e are the coefficients of the term, x is the original one character variable
# that was passed in the original expression and b, d, and f, are the powers
# that x is being raised to in each term and are in decreasing order.
# If the coeficient of a term is zero, the term should not be included.
# If the coeficient of a term is one, the coeficient should not be included.
# If the coeficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coeficient should be included.
# If the power of the term is 1, the carrot and power should be excluded.

# 입력 == 출력
# Test.assert_equals(expand("(x-1)^0"), "1")
# Test.assert_equals(expand("(x-1)^1"), "x-1")
# Test.assert_equals(expand("(x-1)^2"), "x^2-2x+1")
#
# Test.assert_equals(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
# Test.assert_equals(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
# Test.assert_equals(expand("(7x-7)^0"), "1")

# My Code
def expand(expr):
    # 괄호 없애고 ^로 나누어서 분리
    tmp = expr.replace('(', '').replace(')', '').split('^')
    # 지수가 0이면 '1', 1이면 원래 값 반환
    if tmp[1] == '0': return '1'
    elif tmp[1] == '1': return tmp[0]

    # 지수가 1보다 크면 계산
    else:
        # (ax+b)^n
        # 지수 저장
        n = int(tmp[1])

        # 지수 값에 따라서 달라지는 곱해지는 계수 및 상수 구하는 계산
        # : (x+1)^2 = x^2+2x+1 : [1, 2, 1]
        # 계수 : coefficient
        cs = [1, 1]
        for i in range(n + 1):
            cs = [1] + [cs[j]+cs[j+1] for j in range(i-1)] + [1]

        # x, a와 b 구하기 구하기
        a, x, b = 0, '', 0
        for idx, i in enumerate(tmp[0]):
            if i.isalpha():
                x = i
                a = 1 if tmp[0][:idx] == '' else (-1 if tmp[0][:idx] == '-' else int(tmp[0][:idx]))
                b = int(tmp[0][idx+1:])
                break

        # 계산하기
        result = ''
        for idx, c in enumerate(cs):
            # 지수
            new_n = n - idx
            # 계수
            new_c = c * pow(a, new_n) * pow(b, idx)

            # 계수 1, 지수 0이면 1표현, 나머지는 계수
            gyesu = '1' if new_c == 1 else ('-' if new_c == -1 else str(new_c))
            # 지수가 1이면 x만 표현, 나머지는 x+^지수 표현
            jisu = x + ('' if new_n == 1 else f'^{new_n}')

            # 부호 + 계수 + 지수
            # 부호 : 계수가 0보다 작거나 idx가 영 : ''/그 외 '+'
            # 계수 : 지수!=0 and 계수==1 : ''/그 외 : 계수
            # 지수 : 지수==0 : ''/그 외 : 지수
            result += ('' if new_c<0 or idx==0 else '+')+\
                      ('' if new_n !=0 and new_c == 1 else gyesu) + \
                      ('' if new_n == 0 else jisu)
    return result

import re
P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')
def expand_re(expr):
    a, v, b, e = P.findall(expr)[0]
    if e == '0': return '1'
    o = [int(a != '-' and a or a and '-1' or '1'), int(b)]
    e, p = int(e), o[:]
    for _ in range(e - 1):
        p.append(0)
        p = [o[0] * coef + p[i - 1] * o[1] for i, coef in enumerate(p)]
    res = '+'.join(f'{coef}{v}^{e - i}' if i != e else str(coef) for i, coef in enumerate(p) if coef)
    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-', '-')


if __name__=='__main__':
    # print(expand("(x-1)^0"))
    # print(expand("(x-1)^1"))
    print(expand("(-x-1)^2"))
    print(expand("(x-1)^2"))
    print(expand("(x+1)^2"))
    # print(expand("(-2x+1)^2"))
    # print(expand("(2x-1)^2"))
    # print(expand("(5m+3)^4"))
