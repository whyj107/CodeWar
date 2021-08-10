# Even and Odd !
# https://www.codewars.com/kata/594adadee075005308000122/train/python

# 나의 풀이
def even_and_odd(n):
    even = '0'
    odd = '0'
    for i in str(n):
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i
    return (int(even), int(odd))

# 다른 사람의 풀이
def even_and_odd1(n):
    ne = "".join(x for x in str(n) if x in "02468")
    no = "".join(y for y in str(n) if int(y) % 2)
    return tuple(0 if not a else int(a) for a in (ne, no))

import re
odd, even = "[13579]", "[02468]"
def even_and_odd2(n):
    return int("0" + re.sub(odd, "", str(n))), int("0" + re.sub(even, "", str(n)))

print(even_and_odd(126453), (264, 153))
print(even_and_odd(3012), (2, 31))
print(even_and_odd(4628), (4628, 0))