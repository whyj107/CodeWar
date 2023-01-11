# Count consonants
# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python

# 나의 풀이
def consonant_count(s):
    return sum(1 for i in s if (i.isalpha()) and (i.lower() not in 'aeiou'))


print(consonant_count(''), 0)
print(consonant_count('aaaaa'), 0)
print(consonant_count('XaeiouX'), 2)
print(consonant_count('Bbbbb'), 5)
print(consonant_count('helLo world'), 7)
print(consonant_count('h^$&^#$&^elLo world'), 7)
print(consonant_count('0123456789'), 0)
print(consonant_count('012345_Cb'), 2)
