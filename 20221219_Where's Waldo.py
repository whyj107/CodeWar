# Where's Waldo?
# https://www.codewars.com/kata/638244fb08da6c61361d2c40/train/python

# 나의 풀이
def find_waldo(crowd):
    dic = {}
    for i in range(len(crowd)):
        for j in range(len(crowd[i])):
            tmp = crowd[i][j]
            dic.setdefault(tmp, [])
            dic[tmp].append((i, j))
    for k, v in dic.items():
        if len(v) == 1:
            return v[0]

# 다른 사람의 풀이
from collections import defaultdict
def find_waldo1(crowd):
    d = defaultdict(list)
    for y, row in enumerate(crowd):
        for x, c in enumerate(row):
            if c.isalpha():
                d[c].append([y, x])
    return next(v[0] for k, v in d.items() if len(v) == 1)

from collections import Counter
def find_waldo2(crowd):
    flatmap = "".join(crowd)
    waldo = Counter(flatmap).most_common()[-1][0]
    return divmod(flatmap.find(waldo), len(crowd[0]))

print(find_waldo(['             ',
                  '         w   ',
                  '   w         ',
                  '~~~~~~~~~~~~~',
                  '.~..~~.~~~..~',
                  '...P......P..',
                  '......P..P...',
                  '..PW.........']), [7, 3])
print(find_waldo(['                              ',
                  '                              ',
                  '            _                 ',
                  '          _____               ',
                  '        _________             ',
                  '  B  _______________   G   GG ']), [5, 2])
print(find_waldo(['   W         ',
                  '         w   ',
                  '   w    W    ',
                  '~~~~~~~~~~~~~',
                  '....~~...~..~',
                  '.A.P..K.e.P.F',
                  '..#.FfeP.kPk.',
                  '..Pf..f.fAA#.']), [5, 6])
