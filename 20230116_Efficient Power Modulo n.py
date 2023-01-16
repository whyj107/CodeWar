# Efficient Power Modulo n
# https://www.codewars.com/kata/52fe629e48970ad2bd0007e6/train/python

# 나의 풀이
# 거듭제곱의 나머지 : 정수론과 암호학에서 사용됨
# x^y mod n
# if x : 11, y:10, n: 300
# y → 1010(2)
# x^y mod n = (11^(2^1)*11^(2^3)) mod 300
def power_mod(x, y, n):
    result = 1
    while y:
        # y를 2진수로 변형하였을 때 2의 0승이 1인 경우
        if y & 1:
            result = (result * x) % n
        # x는 2 제곱한 뒤 n의 나머지값으로 설정
        x = (x**2) % n
        # 2로 나누기 비트로 표현 → 속도↑
        y >>= 1
    return result

# print(power_mod(2, 3, 5), 3)
# print(power_mod(4, 12, 3), 1)
print(power_mod(11, 10, 300), 1)
# print(power_mod(11, 100000, 49), 32)
# print(power_mod(5, 100000000, 19), 5)