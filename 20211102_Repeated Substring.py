# Repeated Substring
# https://www.codewars.com/kata/5491689aff74b9b292000334/train/python

# 나의 풀이
def f(s):
    d = {}
    for i in range(1, len(s)+1):
        if s.count(s[:i])*s[:i] == s:
            d[s[:i]] = s.count(s[:i])
    return sorted(d.items(), key=lambda x: (x[1], len(x[0])), reverse=True)[0]

# 다른 사람의 풀이
def f1(s):
    for i in xrange(1, len(s) + 1):
        t, k = s[:i], len(s) / i
        if t * k == s:
            return (t, k)


def f2(s):
    m = __import__('re').match(r'^(.+?)\1*$', s)
    return (m.group(1), len(s) / len(m.group(1)))

print(f("ababab"), ("ab", 3));
print(f("abcde"), ("abcde", 1));