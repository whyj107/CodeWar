# V A P O R C O D E
# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

# 나의 풀이
def vaporcode(s):
    return '  '.join([i.upper() for i in s if i != ' '])

# 다른 사람의 풀이
def vaporcode1(s):
    return "  ".join(s.replace(" ", "").upper())

print(vaporcode("Lets go to the movies"), "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
print(vaporcode("Why isn't my code working?"), "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")