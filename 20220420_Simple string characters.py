# Simple string characters
# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

# 나의 풀이
def solve(s):
    result = [0, 0, 0, 0]
    for i in s:
        if i.isupper():
            result[0] += 1
        elif i.islower():
            result[1] += 1
        elif i.isnumeric():
            result[2] += 1
        else:
            result[3] += 1
    return result

# 다른 사람의 풀이
import re
def solve1(s):
    return [len(re.findall(i,s)) for i in ('[A-Z]','[a-z]','\d','[^a-zA-Z0-9]')]

print(solve("Codewars@codewars123.com"), [1, 18, 3, 2])
print(solve("bgA5<1d-tOwUZTS8yQ"), [7, 6, 3, 2])
print(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"), [9, 9, 6, 9])
print(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"), [15, 8, 6, 9])
print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10, 7, 3, 6])
print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7, 13, 4, 10])