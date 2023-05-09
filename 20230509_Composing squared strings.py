# Composing squared strings
# https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

# 나의 풀이
def compose(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    l = len(s1[0])
    return '\n'.join([s1[i][:i+1]+s2[-i-1][:l-i] for i in range(len(s1))])

# 다른 사람의 풀이
def compose2(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]

    n = len(s1)
    out = []

    for i in range(n):
        out.append(s1[i][:i + 1] + s2[i][:(n - i)])

    return "\n".join(out)

print(compose("byGt\nhTts\nRTFF\nCnnI",
              "jIRl\nViBu\nrWOb\nNkTB"),
        "bNkTB\nhTrWO\nRTFVi\nCnnIj")
print(compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"),
        "HgYPW\nTGGbM\nIPhqt\nuUMDH")
