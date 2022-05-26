# int32 to IPv4
# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python

# 나의 풀이
def int32_to_ip(int32):
    result = []
    for _ in range(4):
        int32, ip = divmod(int32, 256)
        result.append(str(ip))
    return '.'.join(result[::-1])

# 다른 사람의 풀이
from ipaddress import IPv4Address
def int32_to_ip1(int32):
    return str(IPv4Address(int32))

def int32_to_ip2(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))

print(int32_to_ip(2154959208), "128.114.17.104")
print(int32_to_ip(0), "0.0.0.0")
print(int32_to_ip(2149583361), "128.32.10.1")