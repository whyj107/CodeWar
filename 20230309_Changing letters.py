# Changing letters
# https://www.codewars.com/kata/5831c204a31721e2ae000294/train/python

# 나의 풀이
def swap(st):
    return st.translate(str.maketrans("aeiou", "AEIOU"))

# 다른 사람의 풀이
def swap1(st):
    return "".join( c.upper() if c in "aeiou" else c for c in st )

print(swap("HelloWorld!"), "HEllOWOrld!")
print(swap("Sunday"), "SUndAy")
print(swap("Codewars"), "COdEwArs")
print(swap("Monday"), "MOndAy")
print(swap("Friday"), "FrIdAy")
print(swap("abracadabra"), "AbrAcAdAbrA")