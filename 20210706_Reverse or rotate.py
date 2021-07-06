# Reverse or rotate?
# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

# 나의 풀이
def revrot(strng, sz):
    if sz == 0: return ""
    strng = [strng[i:i+sz] for i in range(0, len(strng), sz) if len(strng[i:i+sz])>=sz]
    return ''.join([n[::-1] if sum(int(i) for i in n)%2==0 else n[1:]+n[0] for n in strng])

# 다른 사람의 풀이
def revrot1(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""

    while len(s) >= n:
        group = s[:n]
        if sum([int(d) ** 3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]

    return res

def revrot2(strng, sz):
    func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
    return "" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in xrange(0, len(strng) - sz + 1, sz))

def testing(actual, expected):
    print(actual, expected)


testing(revrot("1234", 0), "")
testing(revrot("", 0), "")
testing(revrot("1234", 5), "")
s = "733049910872815764"
testing(revrot(s, 5), "330479108928157")
testing(revrot("123456987653", 6), "234561356789")