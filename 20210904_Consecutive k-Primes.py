# Consecutive k-Primes
# https://www.codewars.com/kata/573182c405d14db0da00064e/train/python

# 풀이를 보고 문제를 이해했다... 단순히 소인수 수라니...

# 다른 사람의 풀이
def primes(n):
    primefac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primefac.append(d)
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return len(primefac)

def consec_kprimes(k, arr):
    return sum(primes(arr[i]) == primes(arr[i + 1]) == k for i in range(len(arr) - 1))


def testing(actual, expected):
    print(actual, expected)

# testing(consec_kprimes(4, [10005, 10030, 10026, 10008, 10016, 10028, 10004]), 3)
# testing(consec_kprimes(3, [10158, 10182, 10184, 10172, 10179, 10168, 10156, 10165, 10155, 10161, 10178, 10170]), 5)
testing(consec_kprimes(2, [10110, 10102, 10097, 10113, 10123, 10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]), 7)
testing(consec_kprimes(2, [10123, 10122, 10132, 10129, 10145, 10148, 10147, 10135, 10146, 10134]), 2)
# testing(consec_kprimes(6, [10176, 10164]), 0)
testing(consec_kprimes(1, [10182, 10191, 10163, 10172, 10178, 10190, 10177, 10186, 10169, 10161, 10165, 10181]), 0)