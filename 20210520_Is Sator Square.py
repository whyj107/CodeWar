# Is Sator Square?
# https://www.codewars.com/kata/5cb7baa989b1c50014a53333/train/python

# 나의 풀이
def is_sator_square(tablet):
    # 왼 오
    l = sorted([''.join(t) for t in tablet])
    print(l)
    # 위 아래
    u = sorted([''.join(t) for t in zip(*tablet)])
    print(u)
    # 오 왼
    r = sorted([''.join(t[::-1]) for t in zip(*tablet)])
    print(r)
    # 아래 위
    d = sorted([''.join(t[::-1]) for t in tablet])
    print(d)
    return l == u == r == d

# 다른 사람의 풀이
def is_sator_square1(tablet):
    return tablet == [t[::-1] for t in tablet][::-1] == list(map(list, zip(*tablet)))

tablet = [['P', 'E', 'R'],
          ['E', 'V', 'E'],
          ['R', 'E', 'P']]
print(is_sator_square(tablet), True)

tablet = [['K', 'N', 'I', 'T'],
          ['N', 'O', 'R', 'I'],  #  warning: O and 0 look similar
          ['I', 'R', '0', 'N'],  #           but are not the same
          ['T', 'I', 'N', 'K']]
print(is_sator_square(tablet), False)

tablet = [['S', 'A', 'T', 'O', 'R'],
          ['A', 'R', 'E', 'P', 'O'],
          ['T', 'E', 'N', 'E', 'T'],
          ['O', 'P', 'E', 'R', 'A'],
          ['R', 'O', 'T', 'A', 'S']]
print(is_sator_square(tablet), True)
