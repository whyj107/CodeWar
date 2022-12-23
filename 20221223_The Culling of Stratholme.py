# The Culling of Stratholme
# https://www.codewars.com/kata/634913db7611b9003dff49ad/train/python

# 나의 풀이
def purify(s: str) -> str:
    print(s)
    result = []
    s = s.split(' ')
    for i in s:
        tmp_s = i
        while ('i' in tmp_s) or ('I' in tmp_s):
            while 'ii' in tmp_s.lower():
                tmp_s = tmp_s.lower().replace('ii', 'i')
            idx = tmp_s.lower().rfind('i')
            if idx == len(tmp_s)-1:
                tmp_s = tmp_s[:idx-1]
            elif idx == 0:
                tmp_s = tmp_s[2:]
            else:
                tmp_s = tmp_s[:idx-1] + ' ' + tmp_s[idx+2:]
        tmp_s = tmp_s.replace(' ', '')
        if tmp_s != '':
            result.append(tmp_s)
    return ' '.join(result)

# 다른 사람의 풀이
from re import sub
def purify1(s):
    return " ".join(word for word in sub(r"(?i)\w?i+\w?", "", s).split())

infected = {'I', 'i'}
def purify2(s):
    return ' '.join(''.join(c for n,c in enumerate(s) if c.isspace() or infected.isdisjoint(s[max(0,n-1):n+2])).split())

print(purify("IabcdefgIhijklmnop"), "bcdefklmnop")
print(purify("CHILI"), "C")
"""
print(purify("The eradication of the citizens of Stratholme"),
      "The eraan of the ens of Stratholme")
print(purify("Kimi Imimi goes to our school"),
      "goes to our school")
print(purify("In heaven all the interesting people are missing"),
      "heaven all the teresg people are g")
print(purify("5I5 i39i9i1 139iii39i i5i9i 1"),
      "13 1")
print(purify("TIL that TIL means Today I learned"),
      "that means Today learned")
print(purify("zippity duppity bopity bip ZIPPITY DUPPITY BOPITY BIP"),
      "y dupy boy Y DUPY BOY")
print(purify("Six sick hicks nick six slick bricks with picks and sticks"),
      "k ks k sk bks h ks and sks")
print(purify("Do not go skiing in the summer"),
      "Do not go sg the summer")
print(purify("Id id ieididi eeiiowe diid owodiid"),
      "ewe owo")
"""