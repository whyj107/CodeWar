# Magnitude
# https://www.codewars.com/kata/5cc70653658d6f002ab170b5/train/python

# 문제를 이해하는 것이 어렵다..... 이게 무슨말이야?
# 풀이
def sqr_modulus(z):
    # 첫번째가 'cart' 혹은 'polar'이고 나머지는 모두 int 형태가 아닐 경우 (False, -1, 1) 반환
    if not (z[0] in ('cart', 'polar') and all(isinstance(x, int) for x in z[1:])):
        return (False, -1, 1)
    # 위의 조건이 맞을 경우 아래의 총합을 구한다.
    # 'cart'의 경우는 복소수 a+bi에서 a^2 + b^2값의 합들이고
    # 'polar'의 경우 (a, b)에서 a^2값들의 합
    sm = sum(
        (re**2 + im**2 for re, im in zip(z[1::2], z[2::2]))
        if z[0] == 'cart' else
        (r**2 for r in z[1::2]))

    # (True, 합, 합을 거꾸로 적은 값)을 반환
    return (True, sm, int(''.join(sorted(str(sm), reverse=True))))


def dotest(z, expect):
    actual = sqr_modulus(z)
    print(actual, expect)

dotest(['cart', 3, 4], (True, 25, 52))
dotest(['polar', "2", 3], (False, -1, 1))
dotest(['cart', 3, 4, 3, 4], (True, 50, 50))
dotest(['polar', 2, 3], (True, 4, 4))
dotest(['polar', 2531, 3261], (True, 6405961, 9665410))